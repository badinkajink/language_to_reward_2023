responses = []
# walk sternly like a patrol dog
response = '''
import numpy as np  # Import numpy for the use of radians conversion

# Set the torso targets for the robot
set_torso_targets(
    target_torso_height=0.4, 
    target_torso_pitch=np.deg2rad(0), 
    target_torso_roll=np.deg2rad(0), 
    target_torso_location_xy=None, 
    target_torso_velocity_xy=(1.0, 0.0), 
    target_torso_heading=None, 
    target_turning_speed=None
)

# Set the stepping parameters for each foot
# front_left foot
set_foot_stepping_parameters(
    foot_name='front_left', 
    stepping_frequency=2.0, 
    air_ratio=0.3, 
    phase_offset=0.0, 
    swing_up_down=0.1, 
    swing_forward_back=0.2, 
    should_activate=True
)

# back_left foot
set_foot_stepping_parameters(
    foot_name='back_left', 
    stepping_frequency=2.0, 
    air_ratio=0.3, 
    phase_offset=0.5, 
    swing_up_down=0.1, 
    swing_forward_back=0.2, 
    should_activate=True
)

# front_right foot
set_foot_stepping_parameters(
    foot_name='front_right', 
    stepping_frequency=2.0, 
    air_ratio=0.3, 
    phase_offset=0.5, 
    swing_up_down=0.1, 
    swing_forward_back=0.2, 
    should_activate=True
)

# back_right foot
set_foot_stepping_parameters(
    foot_name='back_right', 
    stepping_frequency=2.0, 
    air_ratio=0.3, 
    phase_offset=0.0, 
    swing_up_down=0.1, 
    swing_forward_back=0.2, 
    should_activate=True
)

# Execute the plan for the default duration
execute_plan()
'''
responses.append(response)
# walk as if you are preening at a dog show
response = '''
import numpy as np  # Import numpy for angle conversion

# Reset reward since this is a new task
reset_reward()

# Set the torso targets
set_torso_targets(
    target_torso_height=0.35, 
    target_torso_pitch=np.deg2rad(0), 
    target_torso_roll=np.deg2rad(0), 
    target_torso_location_xy=None, 
    target_torso_velocity_xy=(0.5, 0.0), 
    target_torso_heading=None, 
    target_turning_speed=None
)

# Set the foot stepping parameters for all four feet with the specified frequencies, air ratios, and phase offsets
set_foot_stepping_parameters('front_left', 1.0, 0.2, 0.0, 0.05, 0.1, True)
set_foot_stepping_parameters('rear_left', 1.0, 0.2, 0.5, 0.05, 0.1, True)
set_foot_stepping_parameters('front_right', 1.0, 0.2, 0.5, 0.05, 0.1, True)
set_foot_stepping_parameters('rear_right', 1.0, 0.2, 0.0, 0.05, 0.1, True)

# Execute the plan
execute_plan()
'''
responses.append(response)
# walk excitedly
response = '''
import numpy as np  # Import numpy for radian conversion

# Reset reward since this is a new task
reset_reward()

# Set torso targets for the robot
set_torso_targets(
    target_torso_height=0.35,  # Set torso height to 0.35 meters
    target_torso_pitch=np.deg2rad(0),  # Set torso pitch to 0 degrees (converted to radians)
    target_torso_roll=np.deg2rad(0),  # Set torso roll to 0 degrees (converted to radians)
    target_torso_location_xy=None,  # No specific location target
    target_torso_velocity_xy=(1.5, 0.0),  # Move forward at 1.5m/s, no sideways movement
    target_torso_heading=None,  # No specific heading target
    target_turning_speed=None  # No turning speed
)

# Set stepping parameters for each foot
# Front left foot
set_foot_stepping_parameters(
    foot_name='front_left',
    stepping_frequency=3.0,
    air_ratio=0.25,
    phase_offset=0.0,
    swing_up_down=0.08,
    swing_forward_back=0.15,
    should_activate=True
)

# Back left foot
set_foot_stepping_parameters(
    foot_name='rear_left',
    stepping_frequency=3.0,
    air_ratio=0.25,
    phase_offset=0.5,
    swing_up_down=0.08,
    swing_forward_back=0.15,
    should_activate=True
)

# Front right foot
set_foot_stepping_parameters(
    foot_name='front_right',
    stepping_frequency=3.0,
    air_ratio=0.25,
    phase_offset=0.5,
    swing_up_down=0.08,
    swing_forward_back=0.15,
    should_activate=True
)

# Back right foot
set_foot_stepping_parameters(
    foot_name='rear_right',
    stepping_frequency=3.0,
    air_ratio=0.25,
    phase_offset=0.0,
    swing_up_down=0.08,
    swing_forward_back=0.15,
    should_activate=True
)

# Execute the plan for the default duration of 2 seconds
execute_plan()  
'''
responses.append(response)
# walk sadly
response = '''
import numpy as np  # Import numpy for radian conversion

# Set the torso targets
set_torso_targets(
    target_torso_height=0.25, 
    target_torso_pitch=np.deg2rad(0), 
    target_torso_roll=np.deg2rad(0), 
    target_torso_location_xy=None, 
    target_torso_velocity_xy=(0.2, 0.0), 
    target_torso_heading=None, 
    target_turning_speed=None
)

# Set the stepping parameters for each foot
# front_left foot
set_foot_stepping_parameters(
    foot_name='front_left', 
    stepping_frequency=0.5, 
    air_ratio=0.1, 
    phase_offset=0.0, 
    swing_up_down=0.02, 
    swing_forward_back=0.05, 
    should_activate=True
)

# back_left foot
set_foot_stepping_parameters(
    foot_name='back_left', 
    stepping_frequency=0.5, 
    air_ratio=0.1, 
    phase_offset=0.5, 
    swing_up_down=0.02, 
    swing_forward_back=0.05, 
    should_activate=True
)

# front_right foot
set_foot_stepping_parameters(
    foot_name='front_right', 
    stepping_frequency=0.5, 
    air_ratio=0.1, 
    phase_offset=0.5, 
    swing_up_down=0.02, 
    swing_forward_back=0.05, 
    should_activate=True
)

# back_right foot
set_foot_stepping_parameters(
    foot_name='back_right', 
    stepping_frequency=0.5, 
    air_ratio=0.1, 
    phase_offset=0.0, 
    swing_up_down=0.02, 
    swing_forward_back=0.05, 
    should_activate=True
)

# Execute the plan
execute_plan()
'''
responses.append(response)
# walk backwards as if you are really scared
response = '''
import numpy as np  # Import numpy for radian conversion

# Reset the robot's state for the new task
reset_reward()

# Set the torso targets. Since the robot is moving backwards, we use a negative forward velocity.
set_torso_targets(
    target_torso_height=0.2, 
    target_torso_pitch=np.deg2rad(0), 
    target_torso_roll=np.deg2rad(0), 
    target_torso_location_xy=None, 
    target_torso_velocity_xy=(-0.3, 0.0),  # Negative for moving backwards
    target_torso_heading=None, 
    target_turning_speed=None
)

# Set the stepping parameters for each foot, with the specified phase offsets
set_foot_stepping_parameters('front_left', 1.0, 0.15, 0.0, 0.03, 0.05, True)
set_foot_stepping_parameters('rear_left', 1.0, 0.15, 0.5, 0.03, 0.05, True)
set_foot_stepping_parameters('front_right', 1.0, 0.15, 0.5, 0.03, 0.05, True)
set_foot_stepping_parameters('rear_right', 1.0, 0.15, 0.0, 0.03, 0.05, True)

# Execute the plan
execute_plan()
'''
responses.append(response)

responses = responses