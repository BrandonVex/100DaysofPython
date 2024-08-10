from turtle import Screen
from paddle import Paddle

# screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create paddles for pong
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# move paddles
screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")   # Right paddle with Up arrow key
screen.onkey(r_paddle.paddle_down, "Down") # Right paddle with Down arrow key

screen.onkey(l_paddle.paddle_up, "w")   # Left paddle with 'w' key
screen.onkey(l_paddle.paddle_down, "s") # Left paddle with 's' key

# game on
game_on = True
while game_on:
    screen.update()

# screen onclick
screen.exitonclick()
