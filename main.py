#Math programme for Ormiston primary students
#By Celine Bui - Start: 12.07.21
from tkinter import *
from welcome_win import WelcomeWindow
from exercise_win import ExerciseWindow, SideBar
from scoreboard_win import ScoreboardWindow

'''Functions for switching between frames - Ref: https://www.pythontutorial.net/tkinter/tkraise/'''
class SwitchFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(Frame1)

        self.title("Ormiston Computing")
        self.geometry('1000x500')
        self.resizable(False, False)

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
        self.next = Button(self.frame_1, text="LET'S START!", 
                            command=lambda: master.switch_frame(Frame2))
        self.next.grid(column=0, row=0)             
        self.frame_1.grid()

class Frame2(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)

        self.frame_2 = ExerciseWindow(self)
        self.subframe_2 = SideBar(self)
        Button(self, text="STOP!", 
                            command=lambda: master.switch_frame(Frame3)).grid()

        self.frame_2.grid()
        self.subframe_2.grid()

class Frame3(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.frame_3 = ScoreboardWindow(self)
        Button(self.frame_3, text="New Player",
                command=lambda: master.switch_frame(Frame1)).grid()
        self.frame_3.grid()

if __name__ == "__main__":
    root = SwitchFrame()
    root.mainloop()

