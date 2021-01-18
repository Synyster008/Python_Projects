from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
t = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(t)
    canvas.itemconfig(timer, text="00:00")
    check_mark.config(text='')
    title.config(text="Timer")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        time = WORK_MIN*60
        title.config(text="Work!", fg=GREEN)
    else:
        if reps%8!=0:
            time = SHORT_BREAK_MIN*60
            title.config(text="Break", fg=PINK)
        else:
            time = LONG_BREAK_MIN*60
            title.config(text="Break", fg=RED)
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_m = math.floor(count / 60)
    count_s = count % 60

    if count_s < 10:
        count_s = '0' + str(count_s)

    if count_m < 10:
        count_m = '0' + str(count_m)

    canvas.itemconfig(timer, text=f"{count_m}:{count_s}")
    if count > 0:
        global t
        t = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += CHECK_MARK
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

start = Button(text="Start", font=(FONT_NAME, 20, 'bold'), command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", font=(FONT_NAME, 20, 'bold'), command=reset_timer)
reset.grid(column=3, row=3)

check_mark = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=4)

window.mainloop()
