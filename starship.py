from turtle import Turtle
from Bullet import Bullet


class StarShip(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.seth(90)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(0, -400)
        self.shot = 0

    def go_left(self):
        if self.xcor() >= -350:
            self.setx(self.xcor() - 10)

    def go_right(self):
        if self.xcor() <= 350:
            self.setx(self.xcor() + 10)

    def shooting(self):
        bullet = Bullet(self.position())
        bullet.move()
