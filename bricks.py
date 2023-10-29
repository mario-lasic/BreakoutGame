from turtle import Turtle 

ROW_DISTANCE=[0, 80, 160, 240, 320]
COLUMN_DISTANCE=[-400, -300, -200, -100, 0, 100, 200, 300, 400]

class Bricks():
    def __init__(self) -> None:
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        for row in ROW_DISTANCE:
            for column in COLUMN_DISTANCE:
                self.add_brick((column,row))

    def add_brick(self, position):
        new_brick = Turtle(shape="square")
        new_brick.color("red")
        new_brick.penup()
        new_brick.goto(position)
        new_brick.shapesize(stretch_wid=1, stretch_len=3)
        self.bricks.append(new_brick)