import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager= CarManager()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    car_manager.generate_car()
    car_manager.car_move()
    screen.onkey(player.move_up,"Up")
    screen.onkey(player.move_down,"Down")
    if(player.reach_goal()):
        scoreboard.update()
        car_manager.car_speedup()
    for car in car_manager.cars:
        if car.distance(player)<40:
            game_is_on= False
            scoreboard.game_over()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

