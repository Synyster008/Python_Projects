from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = (file.read())
        self.goto(0,260)
        self.penup()
        self.color('white')
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score}", move = False, align = "Center", font = ('Courier', 24, 'normal'))
        self.score +=1

    def reset(self):
        if self.score-1 > int(self.high_score):
            self.high_score = str(self.score-1)
            with open("data.txt", "w") as file:
                file.write(self.high_score)
        self.score = 0
        self.show_score()
