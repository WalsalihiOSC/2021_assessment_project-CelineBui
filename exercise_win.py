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
            return f'{r[1]} x {r[2]} ÷ {r[3]} = ?'
        if r[1] * r[2] / r[3] == a:
            QuestionGenerator.medium()
        return f' ' 

    @staticmethod
    def hard(a, format=True):
        r = random.sample(range(0,1000), 3)
        if format:
            return f'{r[1]} x {r[2]} - {r[3]} = ?'
        if r[1] * r[2] - r[3] == a:
            QuestionGenerator.medium()
        return f' ' 

class SideBar(Frame):
    def __init__(self, master, a):
        Frame.__init__(self, master, background="grey")
        
        self.box = LabelFrame(self, background="orange", width=240, height=350)
        self.box.grid()

        Label(self, text=a).grid(column=0, row=0, padx=45, pady=0)
        self.grid(row=0, column=3, rowspan=3, sticky=E) 

'''Frame 2 - Exercise page'''
class ExerciseWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="blue")

        #White container
        self.white = LabelFrame(self, 
                                width=630, 
                                height=300,
                                background='#D0F6FC') #light blue
        self.white.grid(        column=0, 
                                row=0, 
                                padx=30, 
                                pady=(33, 100))
        self.submit = Button(self.white,
                             text="Submit", command=self.check_answer)
        self.submit.grid(row=3, column=0, columnspan=2, padx=180, pady=(20,20))
        self.label = Label(self.white, text="Answer: ")
        self.label.grid(row=2, column=0, padx=(100,0))

        #Declaring score variable
        self.score = 0

        #Answer box
        self.a = IntVar()
        self.answer = Entry(self.white, textvariable=self.a)
        self.answer.grid(row=2, column=1, padx=(0, 100))
        self.question_generator()
        self.grid()

        #Question number
        self.i = 1
        self.q_num = Label(self.white, 
                           borderwidth=1, 
                           background="yellow", 
                           text=self.i)
        self.q_num.grid(row=0, sticky=W)

    def question_generator(self):
        #To be updated to work with staticmethods above
        self.r = random.sample(range(0,100), 3)
        a = f'{self.r[0]} + {self.r[1]} - {self.r[2]} = ?'
        self.q = Label(self.white, background="#D0F6FC", text=a)
        self.q.grid(row=1, column=0, columnspan=2, padx=200, pady=50) 
    
    def check_answer(self, event=None):
        def clicked():
            self.i = self.i + 1
        self.ans = int(self.answer.get())
        self.question = self.r[0] + self.r[1] - self.r[2]
        if self.ans == self.question:
            self.score += 1
            SideBar(self, 'Correct!')
        else: SideBar(self, 'Incorrect!')
        clicked()
        #Change input field into int
        if self.i <= 10:
            self.calculate()
            self.next_q()
        else: self.store_info()

    def calculate(self):
        
        pass

    def next_q(self):
        self.answer.delete(0, "end")
        self.q.forget()
        self.question_generator()

    def reset(self):
        SideBar.destroy()
        ExerciseWindow.destroy()

    def store_info(self):
        
        self.popup = Button(self.white, text="STOP!", command=quit)
        self.popup.grid()
        #This is where the score calculations
        #are stored into the student's data
        self.reset()
    

    def feedback(self):
        #For addition and subtraction 
        #For multiplication and division
        pass
