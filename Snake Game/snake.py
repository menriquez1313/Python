from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(position)
            self.segment.append(new_seg)    
            
    def move(self):
        #The for loop connects each segment to follow the head. 
        for seg_num in range(len(self.segment) - 1, 0, -1 ):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)