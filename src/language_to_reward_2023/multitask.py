import time
import threading
import subprocess
import os, fcntl, sys
from queue import Queue
import termcolor

# https://github.com/correlllab/MAGPIE/blob/camera_stream/magpie/interprocess.py#L53
########## STREAM COMMUNICATION ####################################################################

def set_non_blocking( output ):
    ''' even in a thread, a normal read with block until the buffer is full '''
    # Original Author, Chase Seibert: https://chase-seibert.github.io/blog/2012/11/16/python-subprocess-asynchronous-read-stdout.html
    fd = output.fileno()
    fl = fcntl.fcntl( fd, fcntl.F_GETFL )
    fcntl.fcntl( fd, fcntl.F_SETFL, fl | os.O_NONBLOCK )

def non_block_read( output ):
    """ Attempt a read from an un-blocked stream, If nothing received, then return empty string """
    # Original Author, Chase Seibert: https://chase-seibert.github.io/blog/2012/11/16/python-subprocess-asynchronous-read-stdout.html
    try:
        out = output.read()
        if out is None:
            # return bytes()
            return None
        # return bytes( out )
        return out
    except:
        # return bytes()
        return None
    
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
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Create a Queue for communication
    input_queue = Queue()

    # Run the user_interaction script in a separate process
    user_interaction_command = [
        "python",
        "-m",
        "language_to_reward_2023.user_interaction",
        "--api_key=" + openai_api_key,
        "--model=gpt-4-1106-preview"
        # "--model=gpt-4"
    ]
    user_interaction_process = subprocess.Popen(
        user_interaction_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,  # Line-buffered for real-time interaction
    )
    set_non_blocking(user_interaction_process.stdout)
    user_interaction_thread = threading.Thread(
        target=lambda: send_user_input(user_interaction_process, "init", input_queue)
    )
    user_interaction_thread.start()
    time.sleep(2)  # Allow some time for initialization

    try:
        # Wait for the subprocess to output the "User:" prompt
        while True:
            output = non_block_read(user_interaction_process.stdout)
            # output = user_interaction_process.stdout
            if output is not None:
                # output = output.readline().strip()
                # print(len(output))
                print(output)

                print(f"Subprocess output: {output}")
                if "User:" in output:
                    break
                time.sleep(1)
        steps = [ "Stand confidently and wait for the cue to start for 3 seconds", 
                 "Begin trotting around the show area elegantly for 5 seconds", 
                 "Perform a playful spin with tail wagging to show excitement for 4 seconds", 
                 "Navigate through an obstacle with precision and focus for 2 seconds", 
                 "Sit with a proud posture, looking at the audience for 3 seconds", 
                 "Finish with a graceful bow to signal the end of the performance for 4 seconds" ] 
        steps = [ "Begin patrolling with a vigilant posture for 10 seconds", 
                 "Stop and scan the area left to right with a focused gaze for 5 seconds", 
                 "Walk with controlled, deliberate steps for another 5 seconds", 
                 "Pause to sniff at a display case curiously for 3 seconds", 
                 "Sit down and observe the visitors calmly for 6 seconds", 
                 "Resume patrolling with an attentive and protective demeanor for 20 seconds"] 
        # Simulate user input and interaction in a continuous loop
        # for user_input in ["walk for 2 seconds", "turn left", "trot excitedly for 2 seconds"]:
        for user_input in steps:
            send_user_input(user_interaction_process, user_input, input_queue)

            # Wait for the subprocess to output the "to continue" message
            while True:
                output = non_block_read(user_interaction_process.stdout)
                # output = user_interaction_process.stdout.readline().strip()
                color = "white"
                if output is not None:
                    output = termcolor.colored(f"\n{output}", f"{color}", attrs=["bold"])
                    if len(output) > 0:
                        print(f"Subprocess output: {output}")
                    if "to continue" in output:
                        send_user_input(user_interaction_process, "yes", input_queue)
                        time.sleep(1)
                        break
            
            while True:
                output = non_block_read(user_interaction_process.stdout)
                if output is not None:
                    if len(output) > 0:
                        print(f"Subprocess output: {output}")
                    if "User:" in output:
                        print("Subprocess output: " + (termcolor.colored(f"\n{output}", "red", attrs=["bold"])))
                        time.sleep(1)
                        break

            # Process the output
            processed_output = input_queue.get()
            print(f"Processed output: {processed_output}\n")
            print(input_queue)
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