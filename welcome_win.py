from tkinter import *
from student import Student

class WelcomeWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)
        self.student = []
        #Interface - blank fields and buttons

        self.sn = StringVar() #Variable for name
        self.name_input = Entry(self, textvariable=self.sn, borderwidth=3)
        self.name_input.grid(column=0, row=0, padx=10, pady=10)

        self.yr = IntVar()
        self.year_level = Entry(self, textvariable=self.yr, borderwidth=3, width=10)
        self.year_level.grid(column=1, row=0, padx=10, pady=10)

        self.conf = Button(self, text="LET'S START!")
        self.conf.grid(column=2, row=4, pady=15, ipady=10, ipadx=10, sticky=E)
        self.conf.configure(command=self.check_info)

        self.diff = IntVar()
        self.diff.set(1) #intialise choices i.e easy

        choices = [ ("Easy", 101),
                    ("Kinda easy", 102),
                    ("Not so easy", 103)]

        self.sideframe = LabelFrame(self, height=10).grid(column=2, row=0)
        for choice, val in choices:
            Radiobutton(self.sideframe,
                        text = choice,
                        indicatoron = 0,
                        width=10,
                        height=3,
                        variable = self.diff,
                        command = self.confirm,
                        value = val).grid(column=2, sticky=W, padx=50, pady=(10,0))

        self.grid()

    def check_info(self):
        if self.sn == " ":
            Label(self, text="Fill in your name!", fg="red").grid(column=0, row=2)
        
    def store_info(self):
        #storing info when user clicks any of the difficulty level buttons to move forward
        self.student.append(self.name_input.get(), self.diff())
        self.confirm()

    def confirm(self):
        '''if len(self.student) == 3:
            self.student[2] = None'''
        Label(self.sideframe, text=f"You've chosen {self.diff} mode!")


    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None

root = Tk()
root.title("Ormiston Computing")
root.geometry("800x320")
WelcomeWindow(root)
root.mainloop()
