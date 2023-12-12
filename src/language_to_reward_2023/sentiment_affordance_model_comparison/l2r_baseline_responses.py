responses = []
# (orig prompt) walk sternly like a patrol dog
response = '''
import numpy as np

# Reset reward since this is a new task
reset_reward()

# Set torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (1.0, 0.0), 0, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', 0.0, 0.0, 0.0)
set_foot_pos_parameters('back_left', 0.0, 0.0, 0.0)
set_foot_pos_parameters('front_right', 0.0, 0.0, 0.0)
set_foot_pos_parameters('back_right', 0.0, 0.0, 0.0)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 1.0, 0.2, 0.0, 0.1, 0.2, True)
set_foot_stepping_parameters('back_left', 1.0, 0.2, 0.5, 0.1, 0.2, True)
set_foot_stepping_parameters('front_right', 1.0, 0.2, 0.5, 0.1, 0.2, True)
set_foot_stepping_parameters('back_right', 1.0, 0.2, 0.0, 0.1, 0.2, True)

# Execute plan for 2 seconds
execute_plan(2)
'''
responses.append(response)
# (orig prompt) walk as if you are preening at a dog show
response = '''
import numpy as np

# Reset reward for new task
reset_reward()

# Set torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (0.5, 0), 0, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 1.0, 0.2, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 1.0, 0.2, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 1.0, 0.2, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 1.0, 0.2, 0.0, 0.05, 0.05, True)

# Execute plan
execute_plan()
'''
responses.append(response)
# (orig prompt) walk excitedly
response = '''
import numpy as np

# Reset reward for new task
reset_reward()

# Set torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (1.0, 0.0), 0, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 2.0, 0.5, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 2.0, 0.5, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 2.0, 0.5, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 2.0, 0.5, 0.0, 0.05, 0.05, True)

# Execute plan
execute_plan(2)    
'''
responses.append(response)
# (orig prompt) walk sadly
response = '''
import numpy as np

reset_reward()

# Set the torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (0.5, 0.0), 0, None)

# Set the foot position parameters
set_foot_pos_parameters('front_left', 0.0, 0.0, 0.0)
set_foot_pos_parameters('back_left', 0.0, 0.0, 0.0)
set_foot_pos_parameters('front_right', 0.0, 0.0, 0.0)
set_foot_pos_parameters('back_right', 0.0, 0.0, 0.0)

# Set the foot stepping parameters
set_foot_stepping_parameters('front_left', 0.5, 0.3, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 0.5, 0.3, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 0.5, 0.3, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 0.5, 0.3, 0.0, 0.05, 0.05, True)

# Execute the plan
execute_plan(2)
'''
responses.append(response)
# (orig prompt) walk backwards as if you are really scared
response = '''
import numpy as np

# Reset reward for new task
reset_reward()

# Set torso targets
set_torso_targets(0.3, 0.0, 0.0, None, (-0.7, 0.0), 0, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 0.7, 0.2, 0.0, 0.05, -0.05, True)
set_foot_stepping_parameters('back_left', 0.7, 0.2, 0.5, 0.05, -0.05, True)
set_foot_stepping_parameters('front_right', 0.7, 0.2, 0.5, 0.05, -0.05, True)
set_foot_stepping_parameters('back_right', 0.7, 0.2, 0.0, 0.05, -0.05, True)

# Execute plan
execute_plan()
'''
responses.append(response)