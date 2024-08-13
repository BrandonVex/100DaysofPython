from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddles for pong
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create ball for pong
ball = Ball()

# scoreboard
scoreboard = Scoreboard()

# move paddles
screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")   # Right paddle with Up arrow key
screen.onkey(r_paddle.paddle_down, "Down") # Right paddle with Down arrow key

screen.onkey(l_paddle.paddle_up, "w")   # Left paddle with 'w' key
screen.onkey(l_paddle.paddle_down, "s") # Left paddle with 's' key

# game on
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect when the ball goes out of bounds on the right side
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
        
    # detect when the ball goes out of bounds on the left side
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()
        
# screen onclick
screen.exitonclick()

