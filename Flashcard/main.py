from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- CREATING DATA FORMAT ------------------------------- #
try:
    data = pandas.read_csv("data/unknown.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words = data.to_dict(orient="records")
    current_word = {}


# ---------------------------- BUTTON FUNCTION ------------------------------- #

def click():
    global words, timer, current_word
    window.after_cancel(timer)
    current_word = choice(words)
    canvas.itemconfig(img, image=front_img)
    canvas.itemconfig(l_title, text="French")
    canvas.itemconfig(l_word, text=current_word['French'])
    timer = window.after(3000, flip)


def click_ok():
    words.remove(current_word)
    print(len(words))
    click()
    new_data = pandas.DataFrame(words)
    new_data.to_csv("data/unknown.csv", index=False)


# ---------------------------- FlIP CARD ------------------------------- #

def flip():
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(l_title, text="English")
    canvas.itemconfig(l_word, text=current_word['English'])


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
img = canvas.create_image(400, 263, image=front_img)
l_title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
l_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2, sticky="EW")

# Buttons
right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=click_ok)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=click)
wrong_button.grid(column=0, row=1)

click()

window.mainloop()
