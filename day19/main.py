import random
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()
screen.setup(width=500,height=400)



#turtle racing game
is_race_on =False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race.? Enter a color")
colors = ["red","orange","green","blue","yellow","purple"]
y_position = [180,120,60,0,-60,-120,-180]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-220, y_position[i])
    all_turtles.append(new_turtle)

is_race_on =True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if(turtle.pos()[0]>=180):
            is_race_on = False
            winner = turtle.color()[0]

if (user_bet== winner):
    print("you win!!")
else:
    print(f"You lose! The {winner} turtle is the winner!!")











### etch-a-sketch app
#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_counter_clockwise():
#     tim.setheading(tim.heading()-10)
#
# def move_clockwise():
#     tim.setheading(tim.heading()+10)
#
# def clear():
#     tim.reset()
#
# screen.listen()
# # listen when the spacebar is pressed , trigger the move_forward function
# a =0
# screen.onkeypress(key="w", fun= move_forward)
# screen.onkeypress(key="s", fun= move_backward)
# screen.onkeypress(key="a", fun= move_clockwise )
# screen.onkeypress(key="d", fun= move_counter_clockwise)
# screen.onkey(key="c", fun= clear)

screen.exitonclick()
