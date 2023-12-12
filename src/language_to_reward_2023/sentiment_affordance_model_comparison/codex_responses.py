responses = []
# walk sternly like a patrol dog
response = '''
reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.45, 0.0, 0.0, None, (0.1, 0.0), None, None)

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
# walk as if you are preening at a dog show
response = '''
reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.45, 0.0, 0.0, None, (0.1, 0.0), None, None)

set_foot_pos_parameters('front_left', 0.0, None, None)
set_foot_pos_parameters('back_left', 0.0, None, None)
set_foot_pos_parameters('front_right', 0.0, None, None)
set_foot_pos_parameters('back_right', 0.0, None, None)
set_foot_stepping_parameters('front_right', 2.0, 0.7, 0.0, 0.1, -0.05, True)
set_foot_stepping_parameters('back_left', 2.0, 0.7, 0.5, 0.1, 0.05, True)
set_foot_stepping_parameters('front_left', 2.0, 0.7, 1.0, 0.1, 0.05, True)
set_foot_stepping_parameters('back_right', 2.0, 0.7, 0.5, 0.1, -0.05, True)
'''
responses.append(response)
# walk excitedly
response = '''
reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.45, 0.0, 0.0, None, (0.1, 0.0), None, None)

set_foot_pos_parameters('front_left', 0.0, None, None)
set_foot_pos_parameters('back_left', 0.0, None, None)
set_foot_pos_parameters('front_right', 0.0, None, None)
set_foot_pos_parameters('back_right', 0.0, None, None)
set_foot_stepping_parameters('front_right', 3.0, 0.7, 0.0, 0.1, -0.05, True)
set_foot_stepping_parameters('back_left', 3.0, 0.7, 0.5, 0.1, 0.05, True)
set_foot_stepping_parameters('front_left', 3.0, 0.7, 1.0, 0.1, 0.05, True)
set_foot_stepping_parameters('back_right', 3.0, 0.7, 0.5, 0.1, -0.05, True)

execute_plan(4)    
'''
responses.append(response)
# walk sadly
response = '''
reset_reward() # This is a new task so reset reward; otherwise we don't need it
set_torso_targets(0.35, 0.0, 0.0, None, (0.1, 0.0), None, None)

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
