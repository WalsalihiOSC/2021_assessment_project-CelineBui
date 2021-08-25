from tkinter import *
from student import Student
from PIL import Image, ImageTk

class WelcomeWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background="#f0f0f0")
        #Interface - blank fields and buttons
        #Logo
        self.im = Image.open('logo-ormmaths.png')
        self.resize = self.im.resize((200, 85), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resize)
        self.img = Label(self, bg="#f2f2f2", image=self.render, height=85, width=170, padx=10)
        self.img.image = self.render
        self.img.grid(column=0, row=2, columnspan=4, sticky=S, ipadx=5, pady=(10,10))
        
        #Entry boxes
        #Code ref for working with textvariable: https://www.geeksforgeeks.org/python-tkinter-entry-widget/
        self.sn = StringVar() #Variable for name
        self.name_input = Entry(self, textvariable=self.sn, borderwidth=3)
        #placeholder text in entry box. Code ref: https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter
        self.name_input.insert(0, "Tell us your name!")
        #delete placeholder text when clicked
        self.name_input.bind("<FocusIn>", 
                                lambda args: self.name_input.delete('0', 'end')) 
        self.name_input.grid(column=0, columnspan=2, row=3, padx=(200, 10), pady=10)
        
        self.yr = IntVar()
        self.year_level = Entry(self, textvariable=self.yr, borderwidth=3, width=15)
        self.year_level.insert(0, "Your year level?") 
        self.year_level.bind("<FocusIn>", 
                                lambda args: self.year_level.delete('0', 'end'))
        self.year_level.grid(column=2, columnspan=2, row=3, padx=(10, 250), pady=10)
        

        self.diff_value = IntVar()
        self.diff_lvl = StringVar()
        self.diff_value.set(1) #intialise choices i.e easy

        choices = [ ("Easy", 101),
                    ("Kinda easy", 102),
                    ("Not so easy", 103)]
        #buttons for difficulty levels
        #Code ref: https://www.python-course.eu/tkinter_radiobuttons.php 
        for choice, val in choices:
            Radiobutton(self,
                        text = choice,
                        indicatoron=0,
                        width=10,
                        height=3,
                        variable = self.diff_value,
                        value = val,
                        command = self.submit).grid(column=1,
                                                     sticky=N,
                                                     columnspan=2,
                                                     padx=(50,50), 
                                                     pady=(10,0))
        self.grid()

    def store_info(self):
        if len(Student.attr_list) == 0:
            Student.attr_list.extend([self.sn.get(), self.yr.get(), self.diff_lvl])
            print(Student.attr_list)
            print(len(Student.attr_list))
            return True
        elif len(Student.attr_list) > 3: 
            #if students choose a different diff lvl
            #i.e clicking 'easy' and then click 'not so easy'
            #Student.attr_list will be reset
            Student.attr_list = []
            return False
        
    
    def check_info(self, event=None):
        self.input_check = 1
        #Drawing value from entry boxes
        #Checking for blanks
        if len(self.sn.get()) == 0:
            Label(self, text="Fill in your name!", fg="red").grid(column=0, row=4)
            self.input_check = 0
        if self.yr.get() == "":
            Label(self, text="Fill in your year level!", fg="red").grid(column=3, row=4)
            self.input_check = 0
        #Invalids and boundaries - year level
        try:
            sy_number = int(self.yr.get())
            return sy_number, True
        except ValueError:
            Label(self, text="You must be in Year 1 to Year 6.", fg="red").grid(column=3, row=4)  
            self.input_check = 0

        if self.yr.get() < 1 or self.yr.get() > 6:
            Label(self, text="You must be in Year 1 to Year 6.", fg="red", bg="#f0f0f0").grid(column=3, row=4)
            self.input_check = 0 

        if self.input_check == 1:
            self.store_info()
           

    def conf_message(self, a):
        Label(self, text=f"You've chosen\n{a} mode!").grid(column=2, columnspan=2,
                                                          row=4, 
                                                          ipadx=10, 
                                                          pady=(20,0))

    def submit(self):
        self.check_info()
        '''if len(self.student) == 3:
            self.student[2] = None'''
        if self.diff_value.get() == 101:
            self.conf_message("Easy")
            self.diff_lvl = "Easy"
        elif self.diff_value.get() == 102:
            self.conf_message("Kinda easy")
            self.diff_lvl = "Kinda easy"
        elif self.diff_value.get() == 103:
            self.conf_message("Not so easy")
            self.diff_lvl = "Not so easy"
        return self.diff_lvl

    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None
