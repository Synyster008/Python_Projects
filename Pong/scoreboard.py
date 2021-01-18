from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.speed("fastest")
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.l_score}", move = False, align = "Center", font = ('Courier', 80, 'normal'))
        self.goto(100,200)
        self.write(f"{self.r_score}", move = False, align = "Center", font = ('Courier', 80, 'normal'))

    def update_l(self):
        self.l_score += 1
        self.show_score()

    def update_r(self):
        self.r_score += 1
        self.show_score()

