FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto((-290, 260))
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.level +=1
        self.write(f"Level:{self.level}", move= False, align= 'left', font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move= False, align= 'center', font= FONT)
