from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # Initialize move_speed here
        
    # function for moving the ball x and y.
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    # function for bouncing the ball.
    def bounce_y(self):
        self.y_move *= -1
        
    # paddle bounce
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Correct the typo here to actually update the move_speed
        
    # reset ball
    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset move_speed when the ball is reset
        self.bounce_x()

# ball = Ball()
# ball.move()
# ball.bounce()
# ball.paddle_bounce()
# ball.reset_ball()
# print(ball.xcor())
        
        
        
    
    
        


        