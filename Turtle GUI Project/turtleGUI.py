from turtle import Turtle, Screen, width
import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


    
#testing Turtle
the_turtle = Turtle()

color_choice = 0
line = 3
shapes = 8
degrees = 360
directions = [0, 90, 180, 270]

#spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        #the_turtle.width(20)
        the_turtle.speed("fastest") 
        the_turtle.color(random_color())
        the_turtle.circle(100)
        the_turtle.seth(the_turtle.heading() + size_of_gap)
        
   
draw_spirograph(5) 

input("Press any key to exit...")
screen = Screen()
screen.exitonclick 