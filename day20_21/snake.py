from turtle import Turtle

Starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_speed = 20


class Snake():
    def __init__(self):
        self.snakeblocks = []
        for position in Starting_positions:
            self.add_block(position)

        self.head = self.snakeblocks[0]

    def move(self):
        for i in range(len(self.snakeblocks) - 1, -1, -1):
            if i == 0:
                self.snakeblocks[0].forward(move_speed)
            else:
                self.snakeblocks[i].goto(self.snakeblocks[i - 1].pos())

    def up(self):
        if self.snakeblocks[0].heading()!=270:
            self.snakeblocks[0].setheading(90)

    def down(self):
        if self.snakeblocks[0].heading() != 90:
            self.snakeblocks[0].setheading(270)

    def left(self):
        if self.snakeblocks[0].heading() != 0:
            self.snakeblocks[0].setheading(180)

    def right(self):
        if self.snakeblocks[0].heading() != 180:
            self.snakeblocks[0].setheading(0)

    def add_block(self,position):
        snakeblock = Turtle()
        snakeblock.shape("square")
        snakeblock.color("white")
        snakeblock.penup()
        snakeblock.goto(position)
        self.snakeblocks.append(snakeblock)

    def extent(self):
        self.add_block(self.snakeblocks[-1].position())