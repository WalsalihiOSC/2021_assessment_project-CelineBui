#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import *
from tkinter import ttk
from student import Student
from welcome_win import WelcomeWindow
from exercise_win import ExerciseWindow, SideBar
from scoreboard_win import ScoreboardWindow
import random


'''Functions for switching between frames - Ref: https://www.pythontutorial.net/tkinter/tkraise/'''
class SwitchFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(WelcomeWindow)

        self.title("Ormiston Computing")
        self.geometry('1000x500')
        self.resizable(False, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()  
    
class WelcomeWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Interface - blank fields and buttons

        self.sn = StringVar() #Variable for name
        self.name_input = Entry(self, textvariable=self.sn, borderwidth=3)
        self.name_input.grid(column=0, row=2, padx=10, pady=10)

        self.yr = IntVar()
        self.year_level = Entry(self, textvariable=self.yr, borderwidth=3, width=10)
        self.year_level.grid(column=1, row=2, padx=10, pady=10)

        Button(self, text="NEXT", command=lambda: master.switch_frame(ExerciseWindow)).grid()

        self.diff_value = IntVar()
        self.diff_value.set(1) #intialise choices i.e easy

        choices = [ ("Easy", 101),
                    ("Kinda easy", 102),
                    ("Not so easy", 103)]
        #buttons for difficulty levels
        #Code ref: https://www.python-course.eu/tkinter_radiobuttons.php 
        for choice, val in choices:
            self.choices = Radiobutton(self,
                                       text = choice,
                        indicatoron = 0,
                        width=10,
                        height=3,
                        variable = self.diff_value,
                        command = self.confirm,
                        value = val).grid(column=2, sticky=W, padx=50, pady=(10,0))
        self.grid()

    def check_info(self):
        self.input_check = 1
        if len(self.name_input.get()) == 0:
            Label(self, text="Fill in your name!", fg="red").grid(column=0, row=1)
            self.input_check = 0
        self.confirm()
        
    def store_info(self):
        #storing info when user clicks any of the difficulty level buttons to move forward
        self.student.append(self.name_input.get(), self.diff())

    def confirm(self):
        '''if len(self.student) == 3:
            self.student[2] = None'''
        if self.diff_value == 101 or 102 or 103:
            self.diff = self.choices.text
            return self.diff
        Label(self, text=f"You've chosen {self.diff} mode!").grid(column=2, row=5)
        self.store_info()

    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None

class ExerciseWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="blue")
        #White container
        self.i = 0
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

        self.a = IntVar()
        self.answer = Entry(self.white, textvariable=self.a)
        self.answer.grid(row=2, column=1, padx=(0, 100))
        self.question_generator()
        self.grid()

    def question_generator(self):
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
            SideBar('Correct!')
        else: SideBar('Incorrect!')
        clicked()
        self.q_num = Label(self.white, 
                           borderwidth=1, 
                           background="yellow", 
                           text=self.i)
        self.q_num.grid(row=0, sticky=W)
        #Change input field into int
        if self.i <= 20:
            self.next_q()
        else: self.complete()

    def next_q(self):
        self.answer.delete(0, "end")
        self.q.forget()
        self.question_generator()

    def complete(self):
        self.popup = Button(self.white, text="STOP!", command=quit)
        self.popup.grid()
        #This is where the score calculations
        #are stored into the student's data
    

    def feedback(self):
        #For addition and subtraction 
        #For multiplication and division
        pass

if __name__ == "__main__":
    root = SwitchFrame()
    root.mainloop()

