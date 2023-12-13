import time
import threading
import subprocess
import os

def simulate_user_input(api_key, user_input):
    command = [
        "python",
        "-m",
        "language_to_reward_2023.user_interaction",
        "--api_key=" + api_key,
    ]
    
    with subprocess.call(
        command,
        stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ) as process:
        # Send user input to the subprocess
        process.stdin.write(user_input + "\n")
        process.stdin.flush()

        # Read and print the subprocess output
        output = process.stdout.readline().strip()
        print(f"User input: {user_input}\nSubprocess output: {output}\n")

def main():
    # Replace this with your actual OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Mock the user inputs for simulation
    mock_inputs = ["your", "list", "of", "user", "inputs"]

    # Run the user_interaction script in a separate thread
    # user_interaction_command = [
    #     "python",
    #     "-m",
    #     "language_to_reward_2023.user_interaction",
    #     "--api_key=" + openai_api_key,
    # ]
    user_interaction_command = [
        "python",
        "src/language_to_reward_2023/test_agent.py",
    ]
    user_interaction_thread = threading.Thread(
        target=subprocess.run,
        args=(user_interaction_command,),
        kwargs={"text": True},
    )
    user_interaction_thread.start()
    time.sleep(2)  # Allow some time for initialization
    user_interaction_thread.join()
    try:
        # Simulate user input and interaction
        for user_input in mock_inputs:
            # simulate_user_input(openai_api_key, user_input)
            time.sleep(1)  # Allow time for processing

    finally:
        user_interaction_thread.join()  # Wait for the user_interaction thread to finish

if __name__ == "__main__":
    main()

    