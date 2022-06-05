STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.sety(self.ycor()+MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor()-MOVE_DISTANCE)

    def reach_goal(self):
        if (self.ycor()>=FINISH_LINE_Y):
            self.goto(STARTING_POSITION)
            return True
        return False