from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 250)
        self.hideturtle()
        self.level = 1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write(arg=f"GAME OVER!", align="center", font=FONT)
