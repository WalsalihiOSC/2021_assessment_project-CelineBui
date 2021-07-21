#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import * 

'''Frame 1 - Welcome page'''
class welcome_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Variables
        self.sn = StringVar()
        
        #Frame
        self.frame = LabelFrame(master)
        self.frame.grid()

        #Interface - blank fields and buttons
        self.name_input = Entry(self.frame, textvariable=self.sn)
        self.name_input.grid(column=0, row=0)
        
        self.easy = Button(self.frame, text="Easy", command=quit)
        self.easy.grid(column=2, row=0)
        self.medium = Button(self.frame, text="Kinda easy", command=quit)
        self.medium.grid(column=2, row=1)
        self.hard = Button(self.frame, text= "Not so easy", command=quit)
        self.hard.grid(column=2, row=2)

    def store_info():
        #storing info when user clicks any of the difficulty level buttons to move forward
        pass


'''Frame 2 - Exercise page'''
class exercise_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Interface design
        self.frame = LabelFrame(master, background="yellow")
        self.frame.grid(column=0, row=0)

        #White container
        self.white = LabelFrame(self.frame, width=130, height=200)
        self.white.grid(column=0, row=0)
        self.q = Label(self.white,
                        text="Auto-generated question")
        self.q.grid(row=0)
        self.label = Label(self.white, text="Answer: ")
        self.label.grid(row=2, column=0)
        self.answer = Entry(self.white)
        self.answer.grid(row=2, column=1)

        self.sidebar = LabelFrame(self.frame, background="blue", width=100)
        self.sidebar.grid(column=3, row=0)

        self.nudge = Label(self.sidebar, text="Star is here to encourage you!")
        self.nudge.grid(column=0, row=0)

    def check_answer(self):
        self.ans = int(self.answer.get())
        #Change input field into int
        pass

    def feedback(self):
        #For addition and subtraction 
        #For multiplication and division
        pass

'''Frame 3 - Scoreboard page'''
class scoreboard_win(Frame):
    class scoreboard_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Interface design
        self.frame = LabelFrame(master, background="orange")
        self.frame.grid(column=0, row=0)

        self.label = Label(self.frame, text="Your score is: ")
        self.label.grid(row=0)
        self.box = Canvas(self.frame, width=50, height=50)
        self.box.grid(row=1, padx=50)
        self.score_display = Label(self.box, text="score variable")
        self.score_display.grid()
        
        self.b1 = Button(self.frame, text="Retry", command=self.retry)
        self.b1.grid(row=3, column=1)
        self.b2 = Button(self.frame, text="New Player", command=self.new_player)
        self.b2.grid(row=3, column=2)

    def calculate_score():
        pass

    def retry():
        pass
    
    def new_player():
        pass


root = Tk()
scoreboard_win(root)
root.title("Ormiston Computing")
root.mainloop()

