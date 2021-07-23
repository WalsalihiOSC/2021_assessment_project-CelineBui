from tkinter import *

'''Frame 3 - Scoreboard page'''
class scoreboard_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Interface design
        self.frame = LabelFrame(master, highlightbackground="orange")
        self.frame.grid(column=0, row=0)

        self.label = Label(self.frame, text="Your score is: ")
        self.label.grid(row=0)
        self.box = Canvas(self.frame, width=50, height=50)
        self.box.grid(row=1, padx=50)
        self.score_display = Label(self.box, text="score variable")
        self.score_display.grid()
        
        self.b1 = Button(self.frame, text="Retry")
        self.b1['command'] = self.retry
        self.b1.grid(row=3, column=1)
        self.b2 = Button(self.frame, text="New Player")
        self.b2['command'] = self.new_player
        self.b2.grid(row=3, column=2)

    def calculate_score():
        pass

    def retry():
        pass
    
    def new_player():
        pass