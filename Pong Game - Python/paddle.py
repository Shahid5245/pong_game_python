from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def up(self):
        self.new_y_position = self.ycor() + 20
        self.goto(x=self.xcor(), y=self.new_y_position)

    def down(self):
        self.new_y_position = self.ycor() - 20
        self.goto(x=self.xcor(), y=self.new_y_position)
