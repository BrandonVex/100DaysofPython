from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    
    # initialize snake
    def __init__(self):
        self.new_turtles = []
        self.create_snake()
        self.head = self.new_turtles[0]
        
    # create snake functions    
    def create_snake(self):
        for turtle_position in STARTING_POSITIONS:
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(turtle_position)
            self.new_turtles.append(new_turtle)
            
    # move snake functions
    def move(self):
        for turtle_num in range(len(self.new_turtles) - 1, 0, -1):
            new_x = self.new_turtles[turtle_num - 1].xcor()
            new_y = self.new_turtles[turtle_num - 1].ycor()
            self.new_turtles[turtle_num].goto(new_x, new_y)
        self.new_turtles[0].forward(MOVE_DISTANCE)

    # control snake functions
    def up(self):
        if self.new_turtles[0].heading() != 270:
            self.new_turtles[0].setheading(UP)
            
    def down(self):
        if self.new_turtles[0].heading() != 90:
            self.new_turtles[0].setheading(DOWN)
    
    def left(self):
        if self.new_turtles[0].heading() != 0:
            self.new_turtles[0].setheading(LEFT)
    
    def right(self):
        if self.new_turtles[0].heading() != 180:
            self.new_turtles[0].setheading(RIGHT)

    