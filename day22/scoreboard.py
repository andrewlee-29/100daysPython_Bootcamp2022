from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.p1score = 0
        self.p2score = 0
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score:{self.p1score} | {self.p2score} ")

    def p1_update(self):
        self.clear()
        self.p1score +=1
        self.write(f"Score:{self.p1score} | {self.p2score} ")

    def p2_update(self):
        self.clear()
        self.p2score += 1
        self.write(f"Score:{self.p1score} | {self.p2score} ")
