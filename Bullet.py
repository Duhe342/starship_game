from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.2, stretch_len=1.5)
        self.seth(90)
        self.location = location
        self.goto(self.location)
        self.color("red")

    def move(self):
        self.forward(20)

    def bullet_contact(self):
        if self.ycor() > 350:
            self.clear()
            self.reset()
            return 1
