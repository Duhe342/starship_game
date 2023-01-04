from turtle import Turtle

POSITIONS = [(-350, 100), (-350, 155), (-295, 100), (-295, 155), (-240, 100), (-240, 155), (-185, 100), (-185, 155),
             (-130, 100), (-130, 155), (-75, 100), (-75, 155), (-20, 100), (-20, 155), (35, 100), (35, 155), (90, 100),
             (90, 155), (145, 100), (145, 155), (200, 100), (200, 155), (255, 100), (255, 155), (310, 100), (310, 155),
             (365, 100), (365, 155)]


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.enemies = []
        self.create_enemies()
        self.hideturtle()

    def create_enemies(self):
        for position in POSITIONS:
            new_enemy = Turtle("square")
            new_enemy.color("white")
            new_enemy.penup()
            new_enemy.goto(position)
            new_enemy.shapesize(stretch_wid=2, stretch_len=2)
            self.enemies.append(new_enemy)
