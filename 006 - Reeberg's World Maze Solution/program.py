def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    while not right_is_clear():
        if not front_is_clear() and not right_is_clear():
            turn_left()
        else:
            move()
    if not at_goal():
        turn_right()
        move()

