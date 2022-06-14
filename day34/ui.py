THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface():
    # make sure the pass in parameter is QuizBrain Object
    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #score Label-----------------
        self.scorelabel = Label(text=f"Score: 0",bg=THEME_COLOR,fg="white")
        self.scorelabel.grid(row=1,column=2)

        #question canvas---------------
        self.canvas =Canvas(width=300,height=250,bg="white")
        self.questiontext = self.canvas.create_text(150,125,text="hello",font=("Arial","20","italic"),width=280)
        self.canvas.grid(row=2,column=1,columnspan=2,pady=50)

        #true button--------------
        #make the button_image not accessable for other classes
        truebutton_image = PhotoImage(file="images/true.png")
        self.truebutton = Button(image=truebutton_image,command=self.true_press)
        self.truebutton.grid(row=3,column=1)
        #wrong button-----------

        falsebutton_image = PhotoImage(file="images/false.png")
        self.falsebutton = Button(image=falsebutton_image,command=self.false_press)
        self.falsebutton.grid(row=3, column=2)

        # set the first question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if (self.quiz.still_has_questions()):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questiontext,text=q_text)
        else:
            self.canvas.itemconfig(self.questiontext,text="You answer all 10 questions")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")
# check answer flash green if they are correct
    def true_press(self):

        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
    def false_press(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
            self.scorelabel.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)