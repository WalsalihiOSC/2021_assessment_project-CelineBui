#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import *
from student import Student

'''Frame 1 - Welcome page'''
class welcome_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #Variables
        self.sn = StringVar()
        self.lvl = StringVar()
        
        #Frame
        self.frame = LabelFrame(master)
        self.frame.pack(fill=BOTH, expand=1)

        #Interface - blank fields and buttons
        self.name_input = Entry(self.frame, textvariable=self.sn)
        self.name_input.pack(pady=50)
        
        self.easy = Button(self.frame, text="Easy", command=quit)
        self.easy.pack(pady=100)
        self.medium = Button(self.frame, text="Kinda easy", command=quit)
        self.medium.pack(pady=100, padx=50)
        self.hard = Button(self.frame, text= "Not so easy", command=quit)
        self.hard.pack(pady=100, padx=150)


root = Tk()
welcome_window(root)
root.title("Ormiston Computing")
root.mainloop()

