from turtle import Turtle, Screen


class Paddle(Turtle ):

    def __init__(self, cord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(cord)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)
    def down(self):
        self.goto(self.xcor(), self.ycor()-20)
