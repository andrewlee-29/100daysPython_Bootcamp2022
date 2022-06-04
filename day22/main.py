#
# Class:
# Scoreboard
# Ball
# Playerpaddle
#
#
# Step:
#
# Create mainscreen
# create playerpaddle and allow user to move
# create ball that can pass through the screen
# dectect collisions with the paddle

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()

paddle = Paddle(350,0)
enemy = Paddle(-350,0)
ball = Ball()
screen.update()
screen.onkey(paddle.moveup, "Up")
screen.onkey(paddle.movedown, "Down")
scoreboard = Scoreboard()
game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    # collision with wall
    if(ball.ycor()<=-280 or ball.ycor()>=280):
        ball.bounce_y()
    # collision with paddle
    if ball.xcor()< 350 and ball.distance(paddle) < 50:
        ball.bounce_x()

    # collision with paddle wall
    if (ball.xcor() <= -380):
        ball.reset_position()
        scoreboard.p1_update()

    if (ball.xcor() >= 380):
        ball.reset_position()
        scoreboard.p2_update()



    screen.onkey(paddle.moveup, "Up")
    screen.onkey(paddle.movedown, "Down")



screen.exitonclick()