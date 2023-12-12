responses = []
# walk sternly like a patrol dog
response = '''
# Set up the torso targets for patrolling
set_torso_targets(0.3, 0, 0, None, (0.5, 0.0), None, None)

#Set foot stepping parameters for a stern patrolling gait
set_foot_stepping_parameters('front_left', 1.5, 0.6, 0.0, 0.05, 0.1, True)
set_foot_stepping_parameters('back_left', 1.5, 0.6, 0.5, 0.05, 0.1, True)
set_foot_stepping_parameters('front_right', 1.5, 0.6, 0.5, 0.05, 0.1, True)
set_foot_stepping_parameters('back_right', 1.5, 0.6, 0.0, 0.05, 0.1, True)
#Execute the plan for the robot to patrol the hallway
execute_plan()
'''
responses.append(response)
# walk as if you are preening at a dog show
response = '''
import numpy as np

# Set up the torso targets for preening walk at a dog show
set_torso_targets(0.4, np.deg2rad(10), 0, None, (0.8, 0.0), None, None)

# Set foot stepping parameters for a preening walk
set_foot_stepping_parameters('front_left', 2.0, 0.4, 0.0, 0.15, 0.2, True)
set_foot_stepping_parameters('back_left', 2.0, 0.4, 0.5, 0.15, 0.2, True)
set_foot_stepping_parameters('front_right', 2.0, 0.4, 0.5, 0.15, 0.2, True)
set_foot_stepping_parameters('back_right', 2.0, 0.4, 0.0, 0.15, 0.2, True)

# Execute the plan for the robot to walk as if it is preening at a dog show
execute_plan()
'''
responses.append(response)
# walk excitedly
response = '''
import numpy as np

# Set up the torso targets for excited walking
set_torso_targets(0.3, 0, 0, None, (1.5, 0.0), None, None)

# Set foot stepping parameters for an excited walk
set_foot_stepping_parameters('front_left', 2.5, 0.7, 0.0, 0.1, 0.15, True)
set_foot_stepping_parameters('back_left', 2.5, 0.7, 0.5, 0.1, 0.15, True)
set_foot_stepping_parameters('front_right', 2.5, 0.7, 0.5, 0.1, 0.15, True)
set_foot_stepping_parameters('back_right', 2.5, 0.7, 0.0, 0.1, 0.15, True)

# Execute the plan for the robot to walk excitedly
execute_plan()    
'''
responses.append(response)
# walk sadly
response = '''
# Set up the torso targets for sad walking
set_torso_targets(0.2, 0, 0, None, (0.3, 0.0), None, None)

# Set foot stepping parameters for a sad walk
set_foot_stepping_parameters('front_left', 1.0, 0.8, 0.0, 0.05, 0.05, True)
set_foot_stepping_parameters('back_left', 1.0, 0.8, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('front_right', 1.0, 0.8, 0.5, 0.05, 0.05, True)
set_foot_stepping_parameters('back_right', 1.0, 0.8, 0.0, 0.05, 0.05, True)

# Execute the plan for the robot to walk sadly
execute_plan()
'''
responses.append(response)
# walk backwards as if you are really scared
response = '''
import numpy as np

# Set up the torso targets for scared backward walking
set_torso_targets(0.2, 0, 0, None, (-0.4, 0.0), None, None)

# Set foot stepping parameters for a scared backward walk
set_foot_stepping_parameters('front_left', 1.2, 0.7, 0.0, 0.05, -0.1, True)
set_foot_stepping_parameters('back_left', 1.2, 0.7, 0.5, 0.05, -0.1, True)
set_foot_stepping_parameters('front_right', 1.2, 0.7, 0.5, 0.05, -0.1, True)
set_foot_stepping_parameters('back_right', 1.2, 0.7, 0.0, 0.05, -0.1, True)

# Execute the plan for the robot to walk backward scaredly
execute_plan()
'''
responses.append(response)