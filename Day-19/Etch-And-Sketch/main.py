from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def back_forwards():
    tim.forward(-10)


def left_rotate():
    tim.left(10)


def right_rotate():
    tim.right(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=back_forwards)
screen.onkey(key="a", fun=left_rotate)
screen.onkey(key="d", fun=right_rotate)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
