from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")

play_game = True
while play_game:
    scoreboard.update_scoreboard()
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.create_snake()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.ycor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -285:
        snake.reset()
        scoreboard.reset()


    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 1:
            snake.reset()
            scoreboard.reset()



screen.exitonclick()



