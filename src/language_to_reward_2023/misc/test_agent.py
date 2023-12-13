import mujoco
from mujoco_mpc import agent as agent_lib
from typing import Optional, Sequence, Mapping, Any

DEFAULT_UI_SERVER_PATH = "/home/wxie/miniconda3/envs/l2r-go1/lib/python3.11/site-packages/language_to_reward_2023/mjpc/l2r_ui_server"
def create_agent(
    task_id: str,
    ui: bool,
    real_time_speed: float = 0.4,
    server_binary_path: Optional[str] = None,
    subprocess_kwargs: Optional[Mapping[str, Any]] = None,
    extra_flags: Optional[Sequence[str]] = None,
) -> agent_lib.Agent:
  """Helper function to create an agent_lib.Agent instance."""
  if server_binary_path is None:
    if ui:
      server_binary_path = DEFAULT_UI_SERVER_PATH

  if ui:
    flags = [
        '--planner_enabled',
    ]
  else:
    flags = []

  return agent_lib.Agent(
      task_id,
      server_binary_path=server_binary_path,
      real_time_speed=real_time_speed,
      extra_flags=flags + (extra_flags or []),
      subprocess_kwargs=subprocess_kwargs,
  )

create_agent("Barkour", True)