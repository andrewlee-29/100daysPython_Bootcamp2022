FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270,250)
        self.write(f"Level: {self.level}",font=FONT)

    def update(self):
        self.clear()
        self.level +=1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over",font=FONT)

