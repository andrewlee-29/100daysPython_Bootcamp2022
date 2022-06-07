from turtle import Turtle,Screen
import pandas as pd
data = pd.read_csv("50_states.csv")
datalist = data.values.tolist()
data["states_low"] = data["state"].map(lambda var: var.lower())
screen= Screen()
screen.setup(width=750,height=500)
screen.bgpic("blank_states_img.gif")

turtle = Turtle()
turtle.hideturtle()
turtle.penup()


game_ison = True
user_data = pd.read_csv("user_data.csv",index_col="index")
# user_data = pd.DataFrame(columns=["state", "x", "y", "states_low"])
print(user_data)
# #imput the data to the map
for i in user_data.index:
    turtle.goto(int(user_data["x"][i]), int(user_data["y"][i]))
    turtle.write(user_data["states_low"][i])

while game_ison :
    num_answer = len(user_data.index)
    input = screen.textinput(f"States Correct{num_answer}/{len(data)}","What's another state name?")
    if (input== None):
        game_ison = False
    elif input.lower() in data["states_low"].values:
        if not(input.lower() in user_data["states_low"].values):
            state_data = data[data["states_low"] == input.lower()]
            turtle.goto(int(state_data.x), int(state_data.y))
            turtle.write(input)
            #store data to csv
            user_data = pd.concat([user_data,state_data])
        else:
            print("repeated answer")
    else:
        print("wrong answer")
user_data.index.name = "index"
user_data.to_csv("user_data.csv")










screen.exitonclick()