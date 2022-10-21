keyword: turtle, drawing, gui, tuple

# Contoh membuat jejak dot

```
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.penup()

def moveWithDot(forwardMove):
    for idx in range(0, forwardMove):
        if idx % 10 == 0:
            timmy_the_turtle.dot()
        timmy_the_turtle.forward(1)
        if idx == forwardMove - 1:
            timmy_the_turtle.right(90)


for _ in range(0, 4):
    moveWithDot(100)

screen = Screen()
screen.exitonclick()
```

# Triangle Drawing

```
from turtle import Turtle, Screen

screen = Screen()

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

color_list = ['red', 'green', 'blue', 'yellow', 'purple']

for idx in range(3, 10):
    get_index_color = idx % len(color_list)
    timmy_the_turtle.color(color_list[get_index_color])
    degre = 360 / idx

    for _ in range(idx):
        timmy_the_turtle.forward(10 * idx)
        timmy_the_turtle.right(degre)


screen.mainloop()
```

# Cara Membuat & Mengakses Tuple

```
my_tupple = (1, 2, 3)
my_tuple[0] # output 1
```

Tuple berbeda dengan list, tupple seperti menulis diatas batu, tidak bisa dihapus dan diubah
```
my_tuppple[0] = 4 # Output Error
```

# Menggambar Spirograph

```
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


draw_spirograph(10)
screen.mainloop()

```