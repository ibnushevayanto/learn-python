from turtle import Turtle
import colorgram
import random

COLOR_LIST = colorgram.extract('hirst_spot_painting.webp', 80)
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    block_of_snake = []

    def __init__(self):
        for index in range(3):
            self.add_block_of_snake(index)

        self.head = self.block_of_snake[0]

    def add_block_of_snake(self, position):
        new_square = Turtle(shape='square')
        new_square.penup()
        new_square.goto(x=position * -20, y=0)
        new_square.color(random.choice(COLOR_LIST).rgb)
        self.block_of_snake.append(new_square)
        

    def move_snake(self):

        for index in range(len(self.block_of_snake) - 1, 0, -1):
            new_x = self.block_of_snake[index - 1].xcor()
            new_y = self.block_of_snake[index - 1].ycor()
            self.block_of_snake[index].goto(new_x, new_y)

        self.head.forward(20)

    def upHandler(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def rightHandler(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def leftHandler(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def downHandler(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
