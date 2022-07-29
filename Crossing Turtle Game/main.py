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