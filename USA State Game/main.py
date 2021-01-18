import turtle
import pandas


def write(x, y, name):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(arg=name, move=False, align="center", font=("Arial", 7, "normal"))


def guess(current_score):
    answer = screen.textinput(title=f"{current_score}/50 States correct", prompt="Name your first state")
    return answer.title()


screen = turtle.Screen()
screen.title("U.S. State Game")
screen.setup(width=740, height=510)
screen.bgpic("blank_states_img.gif")
score = 0
guessed_state = []

data = pandas.read_csv("50_states.csv")
state = data['state'].to_list()

while len(guessed_state) < 50:
    text = guess(score)
    if text in state and text not in guessed_state:
        score += 1
        guessed_state.append(text)
        temp = data[data.state == text]
        x = int(temp.x)
        y = int(temp.y)
        write(x, y, text)

    elif text == 'Exit':
        missing_state = [s for s in state if s not in guessed_state]
        miss = pandas.DataFrame(missing_state)
        miss.to_csv("states to learn.csv")
        break

turtle.mainloop()



