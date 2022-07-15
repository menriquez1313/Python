from tracemalloc import start
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_positions = [(0,0), (-20,0), (-40,0)]
segments =[]
    
for position in starting_positions:
    new_seg = Turtle("square")
    new_seg.penup()
    new_seg.color("white")
    new_seg.goto(position)
    segments.append(new_seg)

game_on = True

 
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1 ):
       new_x = segments[seg_num - 1].xcor()
       new_y = segments[seg_num - 1].ycor()
       segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    













screen.exitonclick()