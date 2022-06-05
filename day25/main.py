from turtle import Turtle,Screen
import pandas as pd
data = pd.read_csv("50_states.csv")
datalist = data.values.tolist()
print(datalist)
states = list(map(lambda var: var.lower(),data["state"].tolist()))
screen= Screen()
screen.setup(width=750,height=500)
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()


game_ison = True
while game_ison :
    input = screen.textinput("States Correct","What's another state name?")
    if input.lower() in states:
        # can't read lowercase
        state_data = data[data.state.str.lower()==input]
        print(state_data)
        turtle.goto(int(state_data.x),int(state_data.y))
        turtle.write(input)
    else:
        game_ison= False



screen.exitonclick()