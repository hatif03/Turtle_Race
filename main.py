from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
y_cor = -200
turtles = []
for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    y_cor += 60
    t.goto(-220, y_cor)
    turtles.append(t)

win_turtle = " "
while win_turtle == " ":
    for i in range(0, 6):
        turtles[i].speed("fastest")
        turtles[i].forward(randint(0, 10))
        if turtles[i].xcor() >= 220:
            win_turtle = colors[i]
            break

if user_bet == win_turtle:
    print(f"You've won! The {win_turtle} turtle is the winner")
else:
    print(f"You've lost! The {win_turtle} turtle is the winner")


screen.exitonclick()
