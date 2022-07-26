from turtle import Screen, Turtle, width 
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen. bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0) #turns off animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()


    
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update() #updates screen after animation is turned off. 
    ball.move()
    
    #Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce()
        
screen.exitonclick()