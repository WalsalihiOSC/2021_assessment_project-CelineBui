from tkinter import *
from student import Student
from PIL import Image, ImageTk

'''Frame 3 - Scoreboard page'''
class ScoreboardWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="#f0f0f0")
        #Logo
        self.im = Image.open('logo-ormmaths.png')
        self.resize = self.im.resize((200, 85), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resize)
        self.img = Label(self, bg="#f2f2f2", image=self.render, height=85, width=170, padx=10)
        self.img.image = self.render
        self.img.grid(column=0, row=0, 
                      ipadx=5, 
                      pady=(10,10),
                      padx=20,
                      sticky=S)

        #Score box label
        self.label = Label(self,
                           text= f"Your score is: ", 
                           font="Helvetica 20",
                           fg="#022575",
                           background="#f0f0f0")
        self.label.grid(row=2, 
                        column=1, 
                        columnspan=3,
                        padx=(50,300),
                        pady=(20,0))
        
        #Score box
        self.box = LabelFrame(self, width=20, height=10)
        self.box.grid(row=3,  
                      column=1, 
                      columnspan=3,
                      padx=(50,300),
                      pady=(0,50))
        self.a = StringVar()
        self.scoreboard(self.a)

        self.grid()

    def scoreboard(self, a):
        self.a = a
        try: 
            self.a = str(Student.attr_list[3])
        except ValueError:
            print("What?")
        self.score_display = Label(self.box,
                                   text=self.a, 
                                   background="#D0F6FC",
                                   font="Helvetica 30",
                                   height=2,
                                   width=10)
        self.score_display.grid()
