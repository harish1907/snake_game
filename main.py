from snake import *
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    for segment in range(3, len(snake.all_segments)):
        if snake.head.distance(snake.all_segments[segment]) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
