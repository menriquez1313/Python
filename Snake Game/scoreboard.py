#This files keeps track of the users score. 

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt",mode="r") as saved_score:
            self.high_score = int(saved_score.read())
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as saved_score:
                saved_score.write(f"{self.high_score}")
            
        self.score = 0
        self.update_score()
        
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)   
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        