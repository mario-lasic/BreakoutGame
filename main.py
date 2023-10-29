from turtle import Screen, Turtle, TurtleScreen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

screen = Screen()
screen.bgcolor("ivory")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

main_paddle = Paddle()
ball = Ball()
screen.onkeypress(main_paddle.go_left, "Left")
screen.onkeypress(main_paddle.go_right, "Right")

bricks = Bricks()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

screen.exitonclick()