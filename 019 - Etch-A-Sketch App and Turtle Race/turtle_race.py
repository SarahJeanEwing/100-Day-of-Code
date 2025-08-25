import random
from turtle import Turtle, Screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle_list.append(turtle)

race_started = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will will the race? Enter a color (" + ", ".join(colors) + ")")


y_position = 140
for i in range(0, len(turtle_list)):
    turtle_list[i].penup()
    turtle_list[i].goto(x=-225, y=y_position)
    y_position -= 50

if user_bet:
    race_started = True

while race_started:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You Win! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You Lose! The {winning_turtle} turtle is the winner!")
            race_started = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()