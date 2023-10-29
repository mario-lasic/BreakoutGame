from turtle import Screen, Turtle, TurtleScreen
from paddle import Paddle
from ball import Ball
from bricks import Bricks

screen = Screen()
screen.bgcolor("ivory")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.listen()

main_paddle = Paddle()
ball = Ball()
screen.onkeypress(main_paddle.go_left, "Left")
screen.onkeypress(main_paddle.go_right, "Right")

bricks = Bricks()


screen.mainloop()