#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import *
from welcome_win import WelcomeWindow
from exercise_win import  ExerciseWindow, QuestionGenerator
from scoreboard_win import ScoreboardWindow
from student import Student

'''Functions for switching between frames - Ref: https://www.pythontutorial.net/tkinter/tkraise/'''
class SwitchFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(Frame1)

        self.title("Ormiston Computing")
        self.geometry('800x400')
        #self.resizable(False, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()  
    
class Frame1(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        self.frame_1 = WelcomeWindow(self)
        self.student = None 
        #Submit button
        self.submit_bttn = Button(self.frame_1, 
                                  text="Submit", 
                                  command=self.submitted, 
                                  highlightbackground="#002a52",
                                  background="#002a52", #navy blue
                                  fg="white"
                                  )
        self.submit_bttn.grid(column=1, 
                              columnspan=2, 
                              row=10, 
                              ipadx=5, ipady=5, 
                              pady=(10,10)
                              )
        self.next = Button(self.frame_1, text="LET'S START!", 
                            command=lambda: master.switch_frame(Frame2),
                            highlightbackground="#002a52")
        

    #Actual submit function is in WelcomeWindow
    #The "Submit" button is to prompt the LET'S START button 
    #in order to move to the next page
    def submitted(self):
        self.frame_1.send_info()
        if self.frame_1.choose_diff() and len(Student.attr_list) == 3:
            print("Double checking in main:", Student.attr_list)
            self.submit_bttn.destroy()
            self.next.grid(column=1, row=10,
                           columnspan=2,
                           ipady=5, ipadx=5,
                           pady=(20,10))

class Frame2(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        if Student.attr_list[2] == 'Easy':
            self.frame_2 = ExerciseWindow(self, QuestionGenerator.easy)
        if Student.attr_list[2] == 'Kinda easy':
            self.frame_2 = ExerciseWindow(self, QuestionGenerator.medium)
        if Student.attr_list[2] == 'Not so easy':
            self.frame_2 = ExerciseWindow(self, QuestionGenerator.hard)

        #Same function as Frame1's button
        self.done_bttn = Button(self.frame_2, 
                                text="DONE", 
                                command=self.submitted,
                                highlightbackground="#002a52",
                                fg="white")
        self.done_bttn.grid(column=0, row=6,
                            columnspan=2, 
                            ipadx=5,
                            ipady=5)
        self.next = Button(self.frame_2, text="YOUR SCORE!", highlightbackground="#D0F6FC",
                            fg="white",
                            command=lambda: master.switch_frame(Frame3))
        self.frame_2.grid()

    def submitted(self):
        #for students to check progress when click done?
        self.left = 10 - self.frame_2.i
        self.error = Label(self, text=f"You have {self.left} questions left!", fg="red", background="#f0f0f0")
        if len(Student.attr_list) == 3:
            self.error.grid(column=0, row=5,
                            columnspan=2, 
                            ipadx=5,
                            ipady=5)
            if self.frame_2.submit():
                self.error.destroy()
        elif len(Student.attr_list) == 4:
            self.done_bttn.destroy()
            self.next.grid(column=0, row=5,
                           columnspan=2, 
                           ipadx=5,
                           ipady=5) 

class Frame3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="#f0f0f0")
        #frame
        self.frame_3 = ScoreboardWindow(self)
        self.object = Student
        self.object.class_obj(self)
        #buttons
        self.b1 = Button(self.frame_3, text="Retry", highlightbackground="#002a52")
        #Assign two functions to one button
        #Code ref: https://www.delftstack.com/howto/python-tkinter/how-to-bind-multiple-commands-to-tkinter-button/
        self.b1['command'] = lambda:[self.object.retry(self), master.switch_frame(Frame2)]
        self.b1.grid(row=4, 
                     column=1, 
                     padx=(50,100),
                     ipadx=10,
                     ipady=10,
                     pady=(0, 150))

        self.b2 = Button(self.frame_3, text="New Player", highlightbackground="#002a52")
        self.b2['command'] = lambda: [self.object.new_player(self), master.switch_frame(Frame1)] #two combined commands in one button
        self.b2.grid(row=4, 
                     column=3, 
                     padx=(0, 300),
                     ipadx=10,
                     ipady=10,
                     pady=(0, 150))

if __name__ == "__main__":
    root = SwitchFrame()
    root.mainloop()

