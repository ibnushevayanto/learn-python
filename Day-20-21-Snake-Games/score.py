from turtle import Turtle

ALIGNMENT = "center"
FONT_STYLE = ("Arial", 24, "normal")


class Score (Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.writeScore()

    def writeScore(self):
        self.write(f"Score : {self.score}",
                   align=ALIGNMENT, font=FONT_STYLE)

    def writeGameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_STYLE)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.writeScore()
