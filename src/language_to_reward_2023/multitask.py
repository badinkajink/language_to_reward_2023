import time
import threading
import subprocess
import os
from queue import Queue

def send_user_input(process, user_input, input_queue):
    # Send user input to the subprocess
    process.stdin.write(user_input + "\n")
    process.stdin.flush()

    # Read and print the subprocess output
    output = process.stdout.readline().strip()
    print(f"User input: {user_input}\nSubprocess output: {output}\n")

    # Put the output into the queue for further processing
    input_queue.put(output)

def main():
    # Replace this with your actual OpenAI API key
    openai_api_key = api_key = os.getenv("OPENAI_API_KEY")

    # Create a Queue for communication
    input_queue = Queue()

    # Run the user_interaction script in a separate process
    user_interaction_command = [
        "python",
        "-m",
        "language_to_reward_2023.user_interaction",
        "--api_key=" + openai_api_key,
    ]
    user_interaction_process = subprocess.Popen(
        user_interaction_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,  # Line-buffered for real-time interaction
    )
    user_interaction_thread = threading.Thread(
        target=lambda: send_user_input(user_interaction_process, "init", input_queue)
    )
    user_interaction_thread.start()
    time.sleep(2)  # Allow some time for initialization

    try:
        # Wait for the subprocess to output the "User:" prompt
        while True:
            output = user_interaction_process.stdout.readline().strip()
            print(f"Subprocess output: {output}")
            if "User:" in output:
                break
            time.sleep(1)

        # Simulate user input and interaction in a continuous loop
        for user_input in ["walk for 2 seconds", "turn left", "trot excitedly for 2 seconds"]:
            send_user_input(user_interaction_process, user_input, input_queue)

            # Wait for the subprocess to output the "to continue" message
            while True:
                output = user_interaction_process.stdout.readline().strip()
                print(f"Subprocess output: {output}")
                if "to continue" in output:
                    if "yes" in output:
                        send_user_input(user_interaction_process, "yes", input_queue)
                        break
                    else:
                        send_user_input(user_interaction_process, "y", input_queue)
                        break
                time.sleep(1)
            
            # while True:
            #     if "User:" in output:
            #         break
            #     time.sleep(1)

            # Process the output
            processed_output = input_queue.get()
            print(f"Processed output: {processed_output}\n")
            time.sleep(1)  # Allow time for processing


    except KeyboardInterrupt:
        # Gracefully handle keyboard interrupt
        pass
    finally:
        # Signal the subprocess to exit gracefully
        user_interaction_process.stdin.write("exit\n")
        user_interaction_process.stdin.flush()
        user_interaction_process.terminate()
        user_interaction_process.wait()
        user_interaction_process.stdout.close()
        user_interaction_thread.join()  # Wait for the user_interaction thread to finish

if __name__ == "__main__":
    main()