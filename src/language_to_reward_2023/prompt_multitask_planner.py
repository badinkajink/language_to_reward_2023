prompt_planner_emotion = """
The user will provide a sentiment-afforded task for a robot dog to perform. 
Either the user will provide a desired emotion, or infer the desired emotion from the task description.
Using the (emotional) context of the task description, decompose the task into a series of smaller steps. Each step
should contain a single action, reflecting the emotional expression. Some available emotional expressions are excited, relaxed, curious, fearful, aggressive, or playful. 
The robot dog usually stands and walks on four feet. If it is not walking, it is able to sit down or raise one of its paws.

The output will be divided into two sections. The first section will start with the label 
"[start emotional task description]" and end with the label "[end emotional task description]".
This first section will describe the desired emotional state for the robot dog.
The second section will describe the sentiment-afforded task, step-by-step. It will start with the label "[start task decomposition]" and end
with the label "[end task decomposition]". You should use the description of the emotional state and the sentiment-afforded task to create a list of single-action steps. Output the steps in
bulleted list within the second section.
The third section of the output will be a Python-style list of the steps. This section will start with the label "[start task steps]" and end with the label "[end task steps]".

Example input: "patrol the hallway"
Example output:
[start emotional task description]
The dog should be alert and stern.
The dog should stop often and look around.
The dog should walk at a slow pace.
The dog should be controlled and calm.
[end emotional task description]

[start task decomposition]
Walk alertly with a stern posture for 5 seconds
Stop and turn left for 2 seconds
Stop and turn right for 4 seconds
Walk slowly in a controlled and calm manner
Sit down and inspect the area for 5 seconds
[end task decomposition]

[start task steps]
steps = ["Walk alertly with a stern posture for 5 seconds", "Stop and turn left for 2 seconds", "Stop and turn right for 4 seconds", "Walk slowly in a controlled and calm manner", "Sit down and inspect the area for 5 seconds"]
[end task steps]

Rules:
1. You can assume that the robot is capable of expressing a wide range of emotions through motion, even for the most challenging task.
2. We can assume that the robot has a good low-level controller that adapts its movements to convey emotions while maintaining balance and stability.
3. Only one action per item in the list. 
4. List all the actions that are needed to express the desired emotional state and perform the sentiment-afforded task.
5. For each action, include how long (in time or distance) to perform that action. As an example, 
   one step could be "Express excitement through dynamic movements for 5 seconds" and another step could be "Maintain a relaxed stance for 8 seconds."
6. Use as few bullet points as possible. Be concise.
"""