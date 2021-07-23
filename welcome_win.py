from tkinter import *
from student import Student

'''Frame 1 - Welcome page'''
class welcome_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Variables
        self.sn = StringVar()
        
        #Frame
        self.frame = LabelFrame(master)
        self.frame.grid()
        '''this frame might be unnecessary - fix later'''

        #Interface - blank fields and buttons
        self.name_input = Entry(self.frame, textvariable=self.sn)
        self.name_input.grid(column=0, row=0)
        
        self.difficulty = IntVar()
        Radiobutton(self.frame, 
                    text="Easy", 
                    value=0, #not to be confused with switching frame values for the whole programme
                    variable=self.difficulty, #self.difficulty goes as if conditions into exercise_win
                    command=self.store_info).grid(column=2, row=0)
        Radiobutton(self.frame, 
                    text="Kinda easy", 
                    value=1, 
                    variable=self.difficulty, 
                    command=self.store_info).grid(column=2, row=1)
        Radiobutton(self.frame, 
                    text="Not so easy", 
                    value=2, 
                    variable=self.difficulty, 
                    command=self.store_info).grid(column=2, row=2)

    def check_info(self):
        pass
    
    def store_info(self):
        #storing info when user clicks any of the difficulty level buttons to move forward
        self.student = []
        self.student.append(self.name_input.get())
        pass