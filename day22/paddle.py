import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(x,y)
        self.xcor()



    def moveup(self):
        self.goto(self.xcor(),self.ycor()+30)
    def movedown(self):
        self.goto(self.xcor(),self.ycor()-30)