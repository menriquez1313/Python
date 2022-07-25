from turtle import Screen, Turtle, width 

screen = Screen()
screen. bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0) #turns off animation

paddle = Turtle()

#User paddle is created
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

game_on = True
while game_on:
    screen.update() #updates screen after animation is turned off. 
    
screen.exitonclick()