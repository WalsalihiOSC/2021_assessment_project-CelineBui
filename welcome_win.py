from tkinter import *
from student import Student

class WelcomeWindow(Frame):
    def __init__(self, container):
        Frame.__init__(self, container, bg="yellow")
        self.student = []
        #Interface - blank fields and buttons
        self.sn = StringVar() #Variable for name
        self.name_input = Entry(self, textvariable=self.sn)
        self.name_input.grid(column=0, row=0)

        self.conf = Button(self, text="That's my name!")
        self.conf.grid(column=0, row=1)
        self.conf.configure(command=self.check_name)

        self.difficulty = IntVar()
        self.b1 = Button(self, 
                        text="Easy",
                        command=self.easy
                        ).grid(column=2, row=0, padx=50, pady=20)
        self.b2 = Button(self, 
                        text="Kinda easy",
                        command=self.med
                        ).grid(column=2, row=1)
        self.b3 = Button(self, 
                        text="Not so easy",
                        command=self.hard
                        ).grid(column=2, row=2)

        self.grid()

    def easy(self):
        self.diff = "Easy"
        self.store_info()
    def med(self):
        self.diff = "Medium"
        self.store_info()
    def hard(self):
        self.diff = "Hard"
        self.store_info()

    def check_name(self):
        if self.sn == " ":
            Label(self, text="Fill in your name!", fg="red").grid(column=0, row=2)
        
    def store_info(self):
        #storing info when user clicks any of the difficulty level buttons to move forward
        self.student.append(self.name_input.get(), self.diff())
        self.check_diff()

    def check_diff(self):
        if len(self.student) == 3:
            self.student[2] = None
        Label(self, text=f"You've chosen {self.diff} mode!")

    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Ormiston Computing')
        self.geometry('800x320')
        self.resizable(False, False)

if __name__ == "__main__":
    root = App()
    WelcomeWindow(root)
    root.mainloop()
