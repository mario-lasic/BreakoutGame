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
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()
    if ball.distance(main_paddle) < 80 and ball.ycor() < -340:
        ball.bounce_y()
    for brick in bricks.bricks:
        difference = brick.ycor() - ball.ycor()
        if ball.distance(brick) < 50 and difference in range(-20, 20):
            print(f"{difference}")
            brick.ht()
            brick.goto(3000,3000)
            bricks.bricks.remove(brick)
            ball.bounce_y()

    if ball.ycor() < - 380:
        game_is_on = False


    if len(bricks.bricks) == 0:
        game_is_on = False
screen.exitonclick()