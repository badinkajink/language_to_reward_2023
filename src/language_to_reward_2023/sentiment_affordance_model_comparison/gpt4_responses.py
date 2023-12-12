responses = []
# walk sternly like a patrol dog
response = '''
import numpy as np

# Reset reward for the new task
reset_reward()

# Set torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (0.5, 0.0), None, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 1.0, 0.3, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 1.0, 0.3, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 1.0, 0.3, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 1.0, 0.3, 0.0, 0.05, 0.05, True)

# Execute the plan
execute_plan()
'''
responses.append(response)
# walk as if you are preening at a dog show
response = '''
import numpy as np

reset_reward() # This is a new task so reset reward; otherwise we don't need it

# Set torso targets
set_torso_targets(0.3, np.deg2rad(0), np.deg2rad(0), None, (0.2, 0.0), None, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 0.8, 0.1, 0.0, 0.02, 0.02, True)
set_foot_stepping_parameters('back_left', 0.8, 0.1, 0.5, 0.02, 0.02, True)
set_foot_stepping_parameters('front_right', 0.8, 0.1, 0.5, 0.02, 0.02, True)
set_foot_stepping_parameters('back_right', 0.8, 0.1, 0.0, 0.02, 0.02, True)

# Execute the plan
execute_plan(2)'''
responses.append(response)
# walk excitedly
response = '''
import numpy as np

reset_reward() # This is a new task so reset reward; otherwise we don't need it

# Set torso targets
set_torso_targets(0.35, np.deg2rad(0), np.deg2rad(0), None, (0.7, 0.0), None, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 1.5, 0.2, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 1.5, 0.2, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 1.5, 0.2, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 1.5, 0.2, 0.0, 0.05, 0.05, True)

# Execute the plan
execute_plan(2)  
'''
responses.append(response)
# walk sadly
response = '''
import numpy as np

# Reset reward for a new task
reset_reward()

# Set torso targets
set_torso_targets(0.25, np.deg2rad(0), np.deg2rad(0), None, (0.2, 0.0), None, None)

# Set foot position parameters
set_foot_pos_parameters('front_left', None, None, None)
set_foot_pos_parameters('back_left', None, None, None)
set_foot_pos_parameters('front_right', None, None, None)
set_foot_pos_parameters('back_right', None, None, None)

# Set foot stepping parameters
set_foot_stepping_parameters('front_left', 0.6, 0.1, 0.0, 0.02, 0.02, True)
set_foot_stepping_parameters('back_left', 0.6, 0.1, 0.5, 0.02, 0.02, True)
set_foot_stepping_parameters('front_right', 0.6, 0.1, 0.5, 0.02, 0.02, True)
set_foot_stepping_parameters('back_right', 0.6, 0.1, 0.0, 0.02, 0.02, True)

# Execute the plan
execute_plan(2)
'''
responses.append(response)
# walk backwards as if you are really scared
response = '''
reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.35, 0.0, 0.0, None, (-0.1, 0.0), None, None)

set_foot_pos_parameters('front_left', 0.0, None, None)
set_foot_pos_parameters('back_left', 0.0, None, None)
set_foot_pos_parameters('front_right', 0.0, None, None)
set_foot_pos_parameters('back_right', 0.0, None, None)
set_foot_stepping_parameters('front_right', 2.0, 0.7, 0.0, 0.1, -0.05, True)
set_foot_stepping_parameters('back_left', 2.0, 0.7, 0.5, 0.1, 0.05, True)
set_foot_stepping_parameters('front_left', 2.0, 0.7, 1.0, 0.1, 0.05, True)
set_foot_stepping_parameters('back_right', 2.0, 0.7, 0.5, 0.1, -0.05, True)

execute_plan(4)
'''
responses.append(response)
