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
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setpos((0,-350))
