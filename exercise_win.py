from tkinter import *
import random

'''this should go in exercise_win.py'''
class QuestionGenerator: 
    @staticmethod
    def easy(a, format=True):
        r = random.sample(range(0,100), 3)
        if format:
            return f'{r[0]} + {r[1]} - {r[2]} = ?'
        if r[0] + r[1] - r[2] == a:
            QuestionGenerator.easy()
        return f' '

    @staticmethod
    def medium(a, format=True):
        r = random.sample(range(0,1000), 3)
        if format:
            return f'{r[1]} x {r[2]} - {r[3]} = ?'
        if r[1] * r[2] - r[3] == a:
            QuestionGenerator.medium()
        return f' ' 

'''Frame 2 - Exercise page'''
class ExerciseWindow(Frame):
    def __init__(self, container):
        super().__init__(container, background="grey")
        #White container
        self.white = LabelFrame(self, 
                                width=530, 
                                height=290,
                                background='#D0F6FC')
        self.white.grid(column=0, 
                        row=0, 
                        padx=20, 
                        pady=20)
        self.q = Label(self.white,
                        text="Auto-generated question")
        self.q.grid(row=0, column=0, columnspan=2, padx=100, pady=20)
        self.label = Label(self.white, text="Answer: ")
        self.label.grid(row=2, column=0, padx=(100,0))

        self.a = IntVar()
        self.answer = Entry(self.white, textvariable=self.a)
        self.answer.grid(row=2, column=1, padx=(0, 100), pady=50)

        self.sidebar = LabelFrame(self, background="blue", height=1000)
        self.sidebar.grid(row=0, column=3, sticky=E)

        self.nudge = Label(self.sidebar, text="Star is here to encourage you!")
        self.nudge.grid(column=0, row=0, padx=20, pady=50)

        self.grid()

    def check_answer(self):
        self.ans = int(self.answer.get())
        #Change input field into int
        pass

    def feedback(self):
        #For addition and subtraction 
        #For multiplication and division
        pass

class ControlFrame:
    def __int__ (self):
        super().__init__(self)

root = Tk()
root.title("Ormiston Computing")
root.geometry("800x320")
ExerciseWindow(root)
root.mainloop()

