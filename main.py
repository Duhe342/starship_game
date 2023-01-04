from turtle import Screen
from starship import StarShip
from enemy import Enemy
from Bullet import Bullet
from scoreboard import ScoreBoard
from time import sleep


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=900)
screen.title("Starship")
screen.tracer(0)

my_scoreboard = ScoreBoard()


my_ship = StarShip()
enemies = Enemy()

number_of_enemies = len(enemies.enemies)

screen.listen()
screen.onkey(my_ship.go_left, "Left")
screen.onkey(my_ship.go_right, "Right")

shot = 0
reload = 0
destroyed = 0


def trigger():
    global shot
    shot = 1


screen.onkey(trigger, "space")


game_is_on = True

while game_is_on:
    sleep(0.01)

    if shot == 1 and reload == 0:
        bullet = Bullet(my_ship.position())
        reload = 1

    if reload == 1:
        bullet.move()

    if reload == 1 and bullet.ycor() > 420:
        bullet.hideturtle()
        reload = 0
        shot = 0

    if reload == 1:
        for enemy in enemies.enemies:
            if bullet.distance(enemy) < 25:
                enemy.goto(500, 900)
                bullet.hideturtle()
                shot = 0
                reload = 0
                destroyed += 1
                my_scoreboard.add_score()
                break

    if destroyed == number_of_enemies:
        my_scoreboard.victory()
        game_is_on = False

    screen.update()

screen.exitonclick()
