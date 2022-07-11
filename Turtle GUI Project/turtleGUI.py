from turtle import Turtle, Screen, width
import random

#testing Turtle
the_turtle = Turtle()
# the_turtle.shape("turtle")
# the_turtle.color("blue")
# the_turtle.dot()
# the_turtle.right(90)
# the_turtle.forward(100)
# the_turtle.right(90)
# the_turtle.forward(100)
# the_turtle.right(90)
# the_turtle.forward(100)
# the_turtle.right(90)


# for x in range(10):
#     the_turtle.forward(10)
#     the_turtle.penup()
#     the_turtle.forward(10)
#     the_turtle.pendown()

colors =["blue", "red", "orange", "green", "pink", "teal", "purple", "brown"]
color_choice = 0
line = 3
shapes = 8
degrees = 360
directions = [0, 90, 180, 270]

# the_turtle.width(10)
# the_turtle.speed(10)
# for x in range(shapes):
#     the_turtle.color(random.choice(colors))
#     for y in range(line):
#         the_turtle.right(degrees/line)
#         the_turtle.forward(100)
#     line += 1
#     color_choice += 1

#random walk
while True:
    the_turtle.width(20)
    the_turtle.speed(10)
    the_turtle.color(random.choice(colors))
    the_turtle.forward(50)
    the_turtle.seth(random.choice(directions))
    

# input("Press any key to exit...")
# screen = Screen()
# screen.exitonclick 