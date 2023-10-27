from turtle import Screen, Turtle, TurtleScreen
from paddle import Paddle

screen = Screen()
screen.bgcolor("ivory")
screen.setup(width=1000, height=800)
screen.title("Breakout")


main_paddle = Paddle()


screen.mainloop()