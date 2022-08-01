from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 240)
        self.update_scorebooard()
        
    def update_scorebooard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font= FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_scorebooard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font= FONT)