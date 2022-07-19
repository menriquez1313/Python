from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
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
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)