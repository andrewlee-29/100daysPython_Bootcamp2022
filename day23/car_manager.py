COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_GENERATE_CHANCE =6

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if(random.randint(1,CAR_GENERATE_CHANCE)==1):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.setx(car.xcor()-self.car_speed)

    def car_speedup(self):
        self.car_speed += MOVE_INCREMENT