from turtle import Turtle, Screen
import colorgram
import random

color_list = colorgram.extract('hirst_spot_painting.webp', 80)

berapa_kolom = int(input("Berapa Kolom: "))
berapa_baris = int(input("Berapa Baris: "))

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.penup()

for baris in range(berapa_baris):
    for kolom in range(berapa_kolom):
        timmy_the_turtle.dot(20, random.choice(color_list).rgb)
        timmy_the_turtle.forward(28)

    if baris % 2 == 0:
        timmy_the_turtle.left(90)
        timmy_the_turtle.forward(28)
        timmy_the_turtle.left(90)
    else:
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(28)
        timmy_the_turtle.right(90)

    timmy_the_turtle.forward(28)


screen.exitonclick()
