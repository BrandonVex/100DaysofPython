from turtle import Screen
from snake import Snake
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# implement snake
snake = Snake()

# control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# exit on click
screen.exitonclick()
