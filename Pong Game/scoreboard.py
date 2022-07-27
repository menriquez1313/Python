from turtle import Turtle

class Scoreboard(Turtle):
    
    #creates scoreboard
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    #draws scoreboard
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))
    
    #point for left side   
    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    #point for right side    
    def r_point(self):
        self.r_score += 1
        self.update_score()