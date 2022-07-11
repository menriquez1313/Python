from turtle import Turtle, Screen

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

#triangle
for x in range(3):
    the_turtle.shape("turtle")
    the_turtle.color("blue")
    the_turtle.right(120)
    the_turtle.forward(100)

#square  
for x in range(4):
    the_turtle.shape("turtle")
    the_turtle.color("red")
    the_turtle.right(90)
    the_turtle.forward(100)

#pentagon
for x in range(5):
    the_turtle.shape("turtle")
    the_turtle.color("orange")
    the_turtle.right(72)
    the_turtle.forward(100)

#hexagon
for x in range(6):
    the_turtle.shape("turtle")
    the_turtle.color("green")
    the_turtle.right(60)
    the_turtle.forward(100)

#heptagon 
for x in range(7):
    the_turtle.shape("turtle")
    the_turtle.color("pink")
    the_turtle.right(51.43)
    the_turtle.forward(100)

#octagon    
for x in range(8):
    the_turtle.shape("turtle")
    the_turtle.color("teal")
    the_turtle.right(45)
    the_turtle.forward(100)

#nonagon  
for x in range(9):
    the_turtle.shape("turtle")
    the_turtle.color("purple")
    the_turtle.right(40)
    the_turtle.forward(100)

#decagon
for x in range(10):
    the_turtle.shape("turtle")
    the_turtle.color("brown")
    the_turtle.right(36)
    the_turtle.forward(100)


input("Press any key to exit...")
screen = Screen()
screen.exitonclick 