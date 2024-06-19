def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
#while at_goal != True:
    #pass_hurdle()

while not at_goal():
    if wall_in_front():
        pass_hurdle()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
