from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# implement snake
snake = Snake()
# implement food
food = Food() 
# scoreboard
scoreboard = Scoreboard()

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
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
        
    # detect collision with tail
    for segment in snake.new_turtles[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


# exit on click!
screen.exitonclick()
