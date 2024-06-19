def turn_right():
    turn_left()
    turn_left()
    turn_left()

def pass_hurdle():
    move()
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
    pass_hurdle()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
