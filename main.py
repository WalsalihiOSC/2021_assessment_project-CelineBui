#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import *
from student import Student

'''this should go in exercise_win.py'''
class QuestionGenerator: 
    @staticmethod
    def easy(a, format=True):
        r = random.sample(range(0,100), 3)
        if format:
            return f'{r[1]} + {r[2]} - {r[3]} = ?'
        if r[1] + r[2] - r[3] == a:
            QuestionGenerator.easy()
        return f' '

    @staticmethod
    def medium(a, format=True):
        r = random.sample(range(0,1000), 3)
        if format:
            return f'{r[1]} x {r[2]} - {r[3]} = ?'
        if r[1] * r[2] - r[3] == a:
            QuestionGenerator.easy()
        return f' '

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
        self.student = Student(self.name_input.get())
        pass
    
'''This class goes with the static methods - probably also into exercise_win'''
'''welcome_win will have own version of ControlFrame for moving to the right exercise frame? + storing info'''
class ControlFrame1(LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Difficulty levels'

        self.difficulty = IntVar()
        Radiobutton(self, 
                    text="Easy", 
                    value=0, #not to be confused with switching frame values for the whole programme
                    variable=self.difficulty, #self.difficulty goes as if conditions into exercise_win
                    command=self.change_frame).grid(column=2, row=0)
        Radiobutton(self, 
                    text="Kinda easy", 
                    value=1, 
                    variable=self.difficulty, 
                    command=self.change_frame).grid(column=2, row=1)
        Radiobutton(self, 
                    text="Not so easy", 
                    value=2, 
                    variable=self.difficulty, 
                    command=self.change_frame).grid(column=2, row=2)

        self.grid(column=1, row=0, sticky='ns')
        #Intialise exercise frames transition
        self.frames = {}

        self.change_frame()

    def change_frame(self):
        self.student.append()
        frame = self.frames[self.difficulty.get()]
        frame.reset()
        frame.tkraise()
        
        
        

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

'''Functions for switching between frames - Ref: https://www.pythontutorial.net/tkinter/tkraise/'''
#This is the main SwitchFrame function for the entire programme - need to see if works
class SwitchFrame:
    def __init__(self, container):
        super().__init__(self, container)

    # initialize frames
        self.main_frames = {}
        self.main_frames[0] = welcome_win(container) #static method in class to be inserted here later?
        self.main_frames[1] = exercise_win(container)
        self.main_frames[2] = scoreboard_win(container)

        self.change_frame()

    def change_frame(self):
        frame = self.main_frames[self.selected_value.get()] #self.selected_value - button with value corresponding with window is clicked
        frame.reset()
        frame.tkraise()


root = Tk()
scoreboard_win(root)
root.title("Ormiston Computing")
root.geometry('1000x500')
root.mainloop()

