from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Score: {self.score}",align="center",font=("Verdana", 15, "normal"))

    def update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}",align="center",font=("Verdana", 15, "normal"))

    def game_over(self):
        self.goto(0, 200)
        self.write("Game over",align="center",font=("Verdana", 15, "bold"))