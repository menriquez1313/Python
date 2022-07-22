#This files keeps track of the users score. 

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)   
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        