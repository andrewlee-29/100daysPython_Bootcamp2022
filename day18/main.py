import turtle
from turtle import *
import random
import colorgram


def turn_move(timmy_the_turtle, n):
    timmy_the_turtle.left(n)
    timmy_the_turtle.forward(100)


def draw_dashedlne(timmy_the_turtle, n):
    for i in range(0, n, 2):
        timmy_the_turtle.forward(5)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(5)
        timmy_the_turtle.pendown()


def random_move(timmy_the_turtle, d, c):
    timmy_the_turtle.left(d)
    timmy_the_turtle.pencolor(c)
    timmy_the_turtle.forward(20)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def chamgepos(timmy_the_turtle,x,y):
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x, y)
    timmy_the_turtle.pendown()

turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")

# draw dot
colors = colorgram.extract('image.jpg', 35)
colors_list=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_list.append((r,g,b))


timmy_the_turtle.penup()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(500)
timmy_the_turtle.setheading(0)
for i in range(0,10):
    for j in range(1,11):
        timmy_the_turtle.forward(70)
        timmy_the_turtle.dot(50, random.choice(colors_list))
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(70)
    if(i%2==0):
        timmy_the_turtle.setheading(180)
    else:
        timmy_the_turtle.setheading(0)
    timmy_the_turtle.back(70)







# # make a spirograph
# gap_size= 5
# for _ in range(int(360/gap_size)):
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.circle(100)
#     timmy_the_turtle.setheading(timmy_the_turtle.heading()+gap_size)
#     print(timmy_the_turtle.heading())


# # random walk
# turtle.colormode(255)
#
# direction_list = [0, 90, 180, 270]
# timmy_the_turtle.pensize(10)
#
# for i in range(0, 50):
#     radom_d = random.choice(direction_list)
#     random_move(timmy_the_turtle, radom_d, random_color())


# #loop draw shape
# angle = 0
# print(angle)
# for j in range(3,11):
#     angle = int(360 / j)
#     for i in range(0,j):
#         turn_move(timmy_the_turtle,angle)


# #draw dashedline
# draw_dashedlne(timmy_the_turtle,100)
#


# Screen
screen = Screen()
screen.exitonclick()
