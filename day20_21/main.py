from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)


game_on = True
snake= Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


print(len(snake.snakeblocks))
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Dectect collision
    #food
    if snake.head.distance(food)< 15 :
        food.refresh()
        snake.extent()
        scoreboard.update_score()

    #wall
    if snake.head.xcor()>=290 or snake.head.xcor()<=-290 or snake.head.ycor()>=290 or snake.head.ycor()<=-290:
        game_on = False
        scoreboard.game_over()

    #tail
    for body in snake.snakeblocks[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
