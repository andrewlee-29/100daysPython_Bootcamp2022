from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed("slow")
        self.x_move=10
        self.y_move=10


    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)