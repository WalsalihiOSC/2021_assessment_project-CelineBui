from tkinter import *

'''Frame 3 - Scoreboard page'''
class ScoreboardWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.label = Label(self, text= f"Your score is: ")
        self.label.grid(row=0, 
                        column=0, 
                        columnspan=3,
                        padx=100,
                        pady=(100,0))
        self.box = LabelFrame(self, width=50, height=50, background="yellow")
        self.box.grid(row=1,  
                      column=0, 
                      columnspan=3,
                      padx=100,
                      pady=(0,50))
        self.score_display = Label(self.box, text="score variable")
        self.score_display.grid()
        
        self.b1 = Button(self, text="Retry")
        self.b1['command'] = self.retry
        self.b1.grid(row=3, column=1, padx=(100,0))
        self.b2 = Button(self, text="New Player")
        self.b2['command'] = self.new_player
        self.b2.grid(row=3, column=2, padx=(100,0))

        self.grid()

    def calculate_score():
        pass

    def retry():
        global selected_value
        selected_value = 0
    
    def new_player():
        pass
