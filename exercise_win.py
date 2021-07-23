'''Frame 2 - Exercise page'''
class exercise_win(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        #Interface design
        self.frame = LabelFrame(master, highlightbackground="yellow")
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