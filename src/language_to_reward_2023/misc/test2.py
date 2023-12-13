import asyncio
import os
import subprocess
import os, fcntl, sys
from queue import Queue

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
            return bytes()
        return bytes( out )
    except:
        return bytes()
    
async def send_user_input(process, user_input, input_queue):
    # Send user input to the subprocess
    process.stdin.write(user_input + "\n")
    process.stdin.flush()

    # Read and print the subprocess output
    output = process.stdout.readline().strip()
    print(f"User input: {user_input}\nSubprocess output: {output}\n")

    # Put the output into the queue for further processing
    input_queue.put(output)

async def main():
    # Replace this with your actual OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Create a Queue for communication
    input_queue = asyncio.Queue()

    # Run the user_interaction script in a separate process
    user_interaction_command = [
        "python",
        "-m",
        "language_to_reward_2023.user_interaction",
        "--api_key=" + openai_api_key,
        "--model=gpt-3.5-turbo"
    ]
    user_interaction_process = await asyncio.create_subprocess_exec(
        *user_interaction_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
        bufsize=0,  # Line-buffered for real-time interaction
    )
    set_non_blocking(user_interaction_process.stdout)
    # await send_user_input(user_interaction_process, "init", input_queue)
    # await asyncio.sleep(2)  # Allow some time for initialization

    try:
        # Wait for the subprocess to output the "User:" prompt
        while True:
            # output = non_block_read(user_interaction_process.stdout).readline().strip()
            output = non_block_read(user_interaction_process.stdout)
            print(f"Subprocess output: {output}")
        #     if b"User:" in output:
        #         break
        #     await asyncio.sleep(1)

        # # Simulate user input and interaction in a continuous loop
        # for user_input in ["walk for 2 seconds", "turn left", "trot excitedly for 2 seconds"]:
        #     await send_user_input(user_interaction_process, user_input, input_queue)

        #     # Wait for the subprocess to output the "to continue" message
        #     while True:
        #         output = (await user_interaction_process.stdout.readuntil()).strip()
        #         print(f"Subprocess output: {output}")
        #         if b"to continue" in output:
        #             await send_user_input(user_interaction_process, "yes", input_queue)
        #             break
        #         await asyncio.sleep(1)

        #     # Process the output
        #     processed_output = await input_queue.get()
        #     print(f"Processed output: {processed_output}\n")
            # await asyncio.sleep(1)  # Allow time for processing

    except asyncio.CancelledError:
        # Gracefully handle coroutine cancellation
        pass
    finally:
        # Signal the subprocess to exit gracefully
        user_interaction_process.stdin.write("exit\n")
        user_interaction_process.stdin.flush()
        user_interaction_process.terminate()
        await user_interaction_process.wait()
        user_interaction_process.stdout.close()

if __name__ == "__main__":
    asyncio.run(main())