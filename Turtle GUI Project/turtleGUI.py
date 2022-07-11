from turtle import Turtle, Screen

#testing Turtle
the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("blue")
the_turtle.dot()
the_turtle.right(90)
the_turtle.forward(100)
the_turtle.right(90)
the_turtle.forward(100)
the_turtle.right(90)
the_turtle.forward(100)
the_turtle.right(90)


for x in range(20):
    the_turtle.forward(10)
    the_turtle.penup()
    the_turtle.forward(10)
    the_turtle.pendown()






input("Press any key to exit...")
screen = Screen()
screen.exitonclick 