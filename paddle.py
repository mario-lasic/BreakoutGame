from turtle import Turtle


class Paddle(Turtle):
    def __init__(
        self,
        shape: str = "classic",
        undobuffersize: int = 1000,
        visible: bool = True,
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.shapesize(stretch_len=6, stretch_wid=0.5)
        self.penup()
        self.setpos((0,-350))

    def go_left(self):
        self.setx(self.xcor() - 10)

    def go_right(self):
        self.setx(self.xcor() + 10)