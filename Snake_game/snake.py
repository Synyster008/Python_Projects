from turtle import Turtle
POS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        for pos in POS:
            self.add_part(pos)
        self.head = self.body[0]

    def add_part(self, pos):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.setpos(pos)
        self.body.append(t)

    def reset(self):
        for parts in self.body:
            parts.goto(1000,1000)
        self.body.clear()
        for pos in POS:
            self.add_part(pos)
        self.head = self.body[0]

    def extend(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            x_pos = self.body[part - 1].xcor()
            y_pos = self.body[part - 1].ycor()
            self.body[part].goto(x_pos, y_pos)
        self.body[0].forward(DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.body[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.body[0].setheading(LEFT)

