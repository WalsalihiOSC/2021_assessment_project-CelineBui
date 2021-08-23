from tkinter import *
from student import Student

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
        if self.diff_value == 101:
            self.diff = "Easy"
        if self.diff_value == 102:
            self.diff = "Kinda easy"
        if self.diff_value == 103:
            self.diff = "Not so easy"
            return self.diff
        Label(self, text=f"You've chosen {self.diff} mode!").grid(column=2, row=5)
        self.store_info()

    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None
