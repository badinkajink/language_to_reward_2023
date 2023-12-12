# Copyright 2023 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A conversational chat utility for controlling MJPC."""

from typing import Any, List

from absl import app
from absl import flags
import colorama
import openai
import termcolor
import time

from language_to_reward_2023 import confirmation_safe_executor
from language_to_reward_2023 import conversation
from language_to_reward_2023 import task_configs

from sentiment_affordance_model_comparison.l2r_baseline_responses import responses as l2r_responses
from sentiment_affordance_model_comparison.chatgpt_plus_responses import responses as chatgpt_plus_responses
from sentiment_affordance_model_comparison.codex_responses import responses as codex_responses

_API_KEY_FLAG = flags.DEFINE_string("api_key", "", "OpenAI API Key")
_TASK_FLAG = flags.DEFINE_enum(
    "task", "barkour", list(task_configs.ALL_TASKS), "task to be used"
)
_PROMPT_FLAG = flags.DEFINE_string(
    "prompt", "thinker_coder", "prompt to be used"
)
_MODEL_FLAG = flags.DEFINE_string(
    "model", "gpt-3.5-turbo", "model to be used"
)
# MODEL = "gpt-4"
MODEL = "gpt-3.5-turbo"

colorama.init()


def main(argv: List[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError("Too many command-line arguments.")

  safe_executor = confirmation_safe_executor.ConfirmationSafeExecutor()

  assert _TASK_FLAG.value in task_configs.ALL_TASKS
  MODEL = _MODEL_FLAG.value
  openai.api_key = _API_KEY_FLAG.value
  task_config = task_configs.ALL_TASKS[_TASK_FLAG.value]
  if _PROMPT_FLAG.value not in task_config.prompts:
    raise ValueError(
        "Invalid value for --prompt. Valid values:"
        f" {', '.join(task_config.prompts)}"
    )
  prompt = task_config.prompts[_PROMPT_FLAG.value]
  print(
      "Starting MJPC UI"
  )
  client_class: Any = task_config.client
  client = client_class(ui=True)

  print(
      "Starting MJPC UI - Initialization complete"
  )

  try:
    # send the grpc channel to the prompt model to create stub
    prompt_model = prompt(
        client, executor=safe_executor
    )
    conv = conversation.Conversation(prompt_model, MODEL)
    client.reset()
    response = '''
import numpy as np  # import numpy because we are using it below

reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.1, np.deg2rad(5), np.deg2rad(15), (2, 3), None, None, np.deg2rad(10))

set_foot_pos_parameters('front_left', 0.1, 0.1, None)
set_foot_pos_parameters('back_left', None, None, 0.15)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', 0.0, 0.0, None)
set_foot_stepping_parameters('front_right', 2.0, 0.5, 0.2, 0.1, -0.05, True)
set_foot_stepping_parameters('back_left', 3.0, 0.7, 0.1, 0.1, 0.05, True)
set_foot_stepping_parameters('front_left', 0.0, 0.0, 0.0, 0.0, 0.0, False)
set_foot_stepping_parameters('back_right', 0.0, 0.0, 0.0, 0.0, 0.0, False)

execute_plan(4)
'''

    reset = '''
reset_reward()
'''
    while True:
      # Final response should be code
      for response in codex_responses:
        try:
          prompt_model.code_executor(response)
          time.sleep(2)
          prompt_model.code_executor(reset)
        except Exception as e:  # pylint: disable=broad-exception-caught
          print("Execution failed, try something else... " + str(e) + "\n")
  finally:
    client.close()
    
  # try:
  #   # send the grpc channel to the prompt model to create stub
  #   prompt_model = prompt(
  #       client, executor=safe_executor
  #   )
  #   conv = conversation.Conversation(prompt_model, MODEL)
  #   client.reset()

  #   while True:
  #     user_command = input(termcolor.colored("User: ", "red", attrs=["bold"]))
  #     # user_command = "nothing"
  #     try:
  #       response = conv.send_command(user_command)
  #     except Exception as e:  # pylint: disable=broad-exception-caught
  #       print("Planning failed, try something else... " + str(e) + "\n")
  #       continue

  #     # Final response should be code
  #     try:
  #       prompt_model.code_executor(response)
  #     except Exception as e:  # pylint: disable=broad-exception-caught
  #       print("Execution failed, try something else... " + str(e) + "\n")
  # finally:
  #   client.close()


if __name__ == "__main__":
  app.run(main)
