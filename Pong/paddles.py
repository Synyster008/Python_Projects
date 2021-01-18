from turtle import Turtle
POS = [(-350, 0), (350, 0)]

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.goto(pos)
        self.color("blue")
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 230:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() > -230:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)