from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the ract? Enter a color: ").lower()
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[index])
    turtles.append(new_turtle)


if user_bet in colors:
    while True:
        index_active = 0
        get_finish = False
        for the_turtle in turtles:
            the_turtle.forward(randint(1, 10))
            if the_turtle.xcor() >= 230:
                get_finish = True
                break
            index_active += 1

        if get_finish == True:
            print(
                f"Your bet is {'correct' if colors[index_active] == user_bet else 'wrong' }, The winner is {colors[index_active]}")
            break
else:
    print("Your bet is invalid")

screen.exitonclick()
