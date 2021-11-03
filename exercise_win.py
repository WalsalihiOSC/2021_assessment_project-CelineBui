from tkinter import *
from student import Student
from PIL import Image, ImageTk
import random

'''this should go in exercise_win.py'''
class QuestionGenerator: 
    global r
    check_var = 0
    selected_var = 0
    @staticmethod
    def easy(format=True):
        global r
        QuestionGenerator.selected_var = 1
        r = random.sample(range(0,10), 3) # 3 random numbers from 0 to 10
        if format:
            return f'{r[0]} + {r[1]} - {r[2]} = ?'
        return r

    @staticmethod
    def medium(format=True):
        global r
        QuestionGenerator.selected_var = 2
        r = random.sample(range(0,100), 3) # 3 random numbers from 0 to 100
        if format:
            return f'{r[0]} + {r[1]} - {r[2]} = ?' 
        return r

    @staticmethod
    def hard(format=True):
        global r
        QuestionGenerator.selected_var = 3
        r = random.sample(range(0,100), 3) # 3 random numbers from 0 to 10
        if format:
            return f'{r[0]} : {r[1]} - {r[2]} = ?'
        return r

    @staticmethod
    def check(a):
        global r
        if QuestionGenerator.selected_var == 1 or QuestionGenerator.selected_var == 2:
            if a == r[0] + r[1] - r[2]:
                QuestionGenerator.check_var = 1
            else:
                QuestionGenerator.check_var = 0
        elif QuestionGenerator.selected_var == 3:
            if a == r[0] / r[1] - r[2]:
                QuestionGenerator.check_var = 1
            else: 
                QuestionGenerator.check_var = 0
            return True
        return True #crucial for submit button to work!!! learnt it the hard way


'''Frame 2 - Exercise page'''
class ExerciseWindow(Frame):

    def __init__(self, master, q_generate):
        Frame.__init__(self, master, height=500,width=800,background="#f0f0f0")
        self.q_generate = q_generate #QuestionGenerator.[chosen difficulty] goes here
        #White container
        self.white = LabelFrame(self, 
                                width=1000, 
                                height=500,
                                background='white',
                                borderwidth=5) 
        self.white.grid(column=0, 
                        row=0, rowspan=5,
                        padx=50, 
                        pady=(30, 30))

        #Logo
        self.im = Image.open('logo-ormmaths.png')
        self.resize = self.im.resize((200, 85), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resize)
        self.img = Label(self, bg="#f2f2f2", image=self.render, height=85, width=170, padx=10)
        self.img.image = self.render
        self.img.grid(column=5, row=0, 
                      columnspan=2, rowspan=3,
                      sticky=S, 
                      ipadx=5, pady=(10,200))

        #Declaring question counter
        self.i = 1
        #for question number to show up as soon as Frame2 initiates
        self.question_count()

        #Answer box
        self.a = IntVar()
        self.answer = Entry(self.white, textvariable=self.a)
        self.answer.grid(row=2, column=1, padx=(0, 110))
        self.question_generator()

        #Declaring score variable
        self.score = 0

        #Submit button
        self.submit = Button(self.white,
                             text="Submit", command=lambda:[self.clicked(), self.question_count()],
                             background="#002a52", 
                             highlightbackground="#002a52", 
                             activebackground="#002a52",
                             fg="white")
        self.submit.grid(row=3, 
                         column=0, 
                         columnspan=2, 
                         padx=180, pady=(30,50), 
                         ipadx=5, ipady=5)
        self.label = Label(self.white, text="Answer: ")
        self.label.grid(row=2, column=0, padx=(120,0))
        self.grid()
    
    def question_generator(self):
        #To be updated to work with staticmethods above
        self.qu = self.q_generate()
        self.q = Label(self.white, background="white", 
                       text=self.qu,
                       font="Helvetica 25", fg="navy blue")
        self.q.grid(row=1, column=0, 
                    columnspan=2, 
                    padx=170, pady=50)
    
    def check_answer(self, event=None):
        self.var = Label(self, background="#f0f0f0", text="") 
        self.checker = QuestionGenerator.check
        try:
            ans = float(self.a.get())
            result = self.checker(ans) #ans = a attribute of check function
            self.var.config(text=result) 
        except ValueError:
            Label(self, "Please enter a number!").grid(column=0, row=0,
                                                       columnspan=2,
                                                       ipadx=5, ipady=5)
        if  QuestionGenerator.check_var == 1:
            #Tick - icon for correct answers
            self.v = Image.open('tick.png')
            self.v_resize = self.v.resize((70, 55), Image.ANTIALIAS)
            self.v_render = ImageTk.PhotoImage(self.v_resize)
            self.tick = Label(self, bg="#f2f2f2", image=self.v_render, height=85, width=100, padx=10)
            self.tick.image = self.v_render

            self.score += 1
            self.icon = self.tick
            self.icon.grid(column=5, row=2, padx=(30,10), pady=(20,0))
            print(self.i, "Correct")

        elif QuestionGenerator.check_var == 0: 
            #Cross - icon for wrong answers
            self.x = Image.open('cross.png')
            self.x_resize = self.x.resize((70, 55), Image.ANTIALIAS)
            self.x_render = ImageTk.PhotoImage(self.x_resize)
            self.cross = Label(self, bg="#f2f2f2", image=self.x_render, height=85, width=100, padx=10)
            self.cross.image = self.x_render

            self.icon = self.cross
            self.icon.grid(column=5, row=2, padx=(30,10), pady=(20,0))
            print(self.i, "Incorrect!")
            return True
        return True
        

    def next_q(self):
        #delete text in entry box when click submit
        #to move on to next question
        self.answer.delete(0, "end")
        self.q.destroy()
        self.question_generator()

    def clicked(self):
        #If self.i = 10 then self.i will not be added 1 - questions stop at 10
        if self.i <= 9 and self.check_answer():
            self.i = self.i + 1
            if self.i < 10:
                self.next_q()
        elif self.i >= 10 and self.check_answer(): 
            #disabling entry box and submit button
            #after the 10th question
            self.answer["state"] = "disabled"
            self.submit["state"] = "disabled"
            self.store_info()
            
    def question_count(self):
        #Question number
        self.q_num = Label(self.white, 
                           borderwidth=1, 
                           background="#002a52", 
                           fg="white",
                           text=self.i)
        self.q_num.grid(row=0, sticky=W)
    

    def store_info(self):
        if len(Student.attr_list) == 3:
            Student.attr_list.extend([f"{self.score}/10"])
            print(Student.attr_list)
            return True
        elif len(Student.attr_list) == 0: 
            return False
        return True
        #This is where the score calculations
        #are stored into the student's data
    
    def reset(self):
        ExerciseWindow.destroy()
