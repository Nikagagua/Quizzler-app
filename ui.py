from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Buttons

        # Images and Buttons
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_button_answer
        )
        self.true_button.grid(column=1, row=2)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_button_answer
        )
        self.false_button.grid(column=0, row=2)

        # Text
        self.score_label = Label(
            text="Score: 0",
            font=("Arial", 15, 'italic'),
            bg=THEME_COLOR,
            fg='white'
        )
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg='green', highlightthickness=0)
            self.window.after(1000, self.change_color)

        else:
            self.canvas.config(bg='red', highlightthickness=0)
            self.window.after(1000, self.change_color)

    def change_color(self):
        self.canvas.config(bg='white')
        self.get_next_question()
