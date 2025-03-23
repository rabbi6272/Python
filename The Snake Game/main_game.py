from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controling the snake 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()    
    time.sleep(0.1)

    # initialize snake on the screen
    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    new_segments = snake.snake[1:]
    for segment in new_segments:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()