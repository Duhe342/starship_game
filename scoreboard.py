from turtle import Turtle
ALINGMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 400)
        self.score = 0
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}", align=ALINGMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.refresh_scoreboard()

    def victory(self):
        self.goto(0, 0)
        self.write("You won", align=ALINGMENT, font=FONT)


