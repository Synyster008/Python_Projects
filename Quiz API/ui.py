THEME_COLOR = "#375362"
FONT=("Arial", 20, 'italic')
from tkinter import *

class QuizUI:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)
        self.score_label = Label(text='Score: 0', bg= THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125, text='', width=280, fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        r_img = PhotoImage(file="images/true.png")
        w_img = PhotoImage(file="images/false.png")
        self.r_button = Button(image=r_img, highlightthickness=0, command=self.r_check)
        self.w_button = Button(image=w_img, highlightthickness=0, command=self.w_check)
        self.r_button.grid(column=0, row=2)
        self.w_button.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q)
        else:
            self.canvas.itemconfig(self.question, text='FIN')
            self.r_button.config(state='disabled')
            self.w_button.config(state='disabled')

    def r_check(self):
        self.feedback(self.quiz.check_answer('True'))

    def w_check(self):
        self.feedback(self.quiz.check_answer('False'))

    def feedback(self, ans):
        if ans:
            self.canvas.config(bg='green')
        else:
            self.canvas.config( bg='red')
        self.window.after(1000, self.next_question)