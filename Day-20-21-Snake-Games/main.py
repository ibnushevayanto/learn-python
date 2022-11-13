from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.upHandler)
screen.onkey(key='Right', fun=snake.rightHandler)
screen.onkey(key='Left', fun=snake.leftHandler)
screen.onkey(key='Down', fun=snake.downHandler)

IS_GAME_OVER = False

while IS_GAME_OVER == False:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Mendeteksi jika kepala memakan makanan
    if snake.head.distance(food) < 15:
        food.changeLocation()
        snake.add_block_of_snake(len(snake.block_of_snake))
        score.increaseScore()

    # Mendeteksi jika keluar pagar
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.writeGameOver()
        IS_GAME_OVER = True

    # Mendeteksi apakah kepala mengenai tubuh
    for circle in snake.block_of_snake[1:]:
        if snake.head.distance(circle) < 10:
            score.writeGameOver()
            IS_GAME_OVER = True

screen.exitonclick()
