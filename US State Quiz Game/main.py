import turtle
import csv
import pandas

#creates the screen
screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#creates the turtle that marks state on map
state_name = turtle.Turtle()
state_name.penup()
state_name.hideturtle()

#opens CSV file
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()


guess = 0
while guess < 50:
    answer_state = screen.textinput(title=f"{guess}/50 States Guessed", prompt="Guess a State or Type 'Exit'")
    if answer_state == "Exit":
        break
    for state in states_list:
        if state.lower() == answer_state.lower():
            x = int(data.x[data.state == state])
            y = int(data.y[data.state == state])
            
            state_name.goto(x,y)
            state_name.write(state)
            
            states_list.remove(state)
            guess += 1
        
print("Thank you for playing!")
            