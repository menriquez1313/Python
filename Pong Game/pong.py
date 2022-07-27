from turtle import Screen, Turtle, width 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen. bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0) #turns off animation

line = Turtle()
score = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

#up and down keys for both paddles
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

line.color("white")
line.hideturtle()
line.goto(0,400)
line.goto(0,-400)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update() #updates screen after animation is turned off. 
    ball.move()
    
    #Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
        
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        #print("made contact")
        ball.bounce_x()
        
    #Detect when ball goes passed either paddles
    #Left paddle
    if ball.xcor() > 360:
        #print("GG's")
        score.l_point()
        ball.reset_position()
    
    #Right paddle    
    if ball.xcor() < -360:
        #print("GG's")
        score.r_point()
        ball.reset_position()
        
screen.exitonclick()