import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Turtle and Car
player = Player()
car_manage = CarManager()

screen.listen()
screen.onkey(player.go_up,"Up")

#Car's are generated here. 
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manage.create_car()
    car_manage.move_car()
    
    #Detects car collision
    for car in car_manage.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            
    #Detects successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manage.level_up()




screen.exitonclick()