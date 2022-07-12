from turtle import Turtle, Screen, color
import turtle as t
import random
import colorgram

#Colorgram extracts colors from an image.
#Only used when color is needed from an image. Extract colors and paste it onto 'color_list'.
# rgb_colors = []
# colors = colorgram.extract('The Hirst Painting Project/image.jpg', 30)
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

t.colormode(255) #To input RGB

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), 
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), 
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]



def make_dots(lines):
    for x in range(int(lines)):
        the_turtle.home()
        for y in range(10):
            the_turtle.penup()
            the_turtle.dot(20, random.choice(color_list))
            the_turtle.forward(50)
        the_turtle.seth(90)
        the_turtle.forward(50)
            
the_turtle = t.Turtle()
lines = int(input("How many lines of dots?:" ))

make_dots(lines)

input("Press any key to exit...")
screen = Screen()
screen.exitonclick 