#Small Turtle Race Project

from turtle import Turtle, Screen, turtles
import random
import turtle


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange","yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True
else:
    print("No bet, no race! Goodbye!")
    exit()
    
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Winner! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry. The winner is {winning_color} turtle. :( ")
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance) #moves current turtle from All_turtle list
        
        

screen.exitonclick()