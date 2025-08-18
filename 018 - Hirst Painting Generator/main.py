from turtle import Turtle, Screen
import random

TURTLE_SIZE = 20
color_list = [(248, 233, 233), (236, 68, 68), (44, 187, 187), (209, 158, 158), (228, 52, 52), (107, 200, 200), (55, 102, 102), (206, 55, 55), (190, 43, 43), (219, 128, 128), (203, 8, 8), (103, 170, 170), (102, 111, 111), (24, 136, 136), (194, 169, 169), (42, 175, 175), (40, 47, 47), (152, 218, 218), (218, 229, 229), (187, 19, 19), (231, 167, 167), (14, 97, 97), (12, 24, 24), (236, 169, 169), (5, 65, 65), (253, 6, 6)]
screen = Screen()
screen.colormode(255)
tim = Turtle(shape="circle", visible=False)
tim.speed(0)
tim.penup()
start_position_x = -360
start_position_y = -300
tim.goto(start_position_x, start_position_y)

for _ in range(13):
    tim.goto(start_position_x, start_position_y)
    for _ in range(17):
        tim.forward(39)
        tim.dot(20, random.choice(color_list))
    start_position_y += 50

screen.exitonclick()