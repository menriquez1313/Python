from tracemalloc import start
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments =[]
    
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    #Detect collision with food. 
    if snake.head.distance(food) < 15:
        print("Ate food!")
        food.refresh()
        snake.extend() 
        score.increase_score()
        
    #Detect collision with wall. 
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print("GG's! GAME OVER")
        score.game_over()
        game_on = False
    
    #Detect collision with Tail. 
    # for segment in snake.segment:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_on = False
    #         score.game_over()
    
    #Practicing SLICING
    for seg in snake.segment[1::]: #takes every segment EXCEPT for the 1st on in position 0
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()
        
            
            #if head collides with any segment in the tail
            #GAME OVER!



screen.exitonclick()