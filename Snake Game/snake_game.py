from tracemalloc import start
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

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
    
    for snake in segments:
        snake.forward(1)
    













screen.exitonclick()