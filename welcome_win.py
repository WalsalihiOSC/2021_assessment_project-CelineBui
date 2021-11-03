from tkinter import *
from student import Student, CheckingInput
from PIL import Image, ImageTk

class WelcomeWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, height=500, width=800, background="#f0f0f0")
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
        self.name_input.grid(column=0, columnspan=2, row=4, padx=(200, 10), pady=10) ########       FIX HERE!
        
        #though declare as sringvar to avoid complications with placeholder text
        #only string convertible to int var accepted through checking
        self.yr = Entry(self, borderwidth=3, width=15)
        self.yr.insert(0, "Your year level?") 
        #delete placeholder text when clicked
        self.yr.bind("<FocusIn>", 
                    lambda args: self.yr.delete('0', 'end'))
        self.yr.grid(column=2, columnspan=2, row=4, padx=(10, 250), pady=10) ########       FIX HERE!
        

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
                        indicatoron=0, #to transform checkbuttons into boxes
                        width=10,
                        height=2,
                        variable = self.diff_value,
                        value = val,
                        command = self.choose_diff).grid(column=1,
                                                     sticky=N,
                                                     columnspan=2,
                                                     padx=(50,50), 
                                                     pady=(10,0))
                                #self.submit refers to the numerical values in 'choices' list
                                #to input text (e.g 'Easy') for the third item (diff_lvl) in attr_list
        self.grid()

    def store_info(self):
        if len(Student.attr_list) == 0:
            Student.attr_list.extend([self.sn.get(), self.yr.get(), self.diff_lvl])
            print("Accurate information stored:", Student.attr_list)
            return True
        else:
            Student.attr_list = []
            return False

    #   Error labels
    def errors(self, event=None):
        self.input_check = 1
        #Drawing value from entry boxes
        #Checking for blanks
        
        #Invalids and boundaries - year level
        if CheckingInput.invalid == 2 and self.yr.get() != 'Your year level?' and self.yr.get() != '':
            self.err_3 = Label(self, text="Please write your year level\nin numbers.", fg="red", bg="#f0f0f0")
            self.err_3.grid(column=2, columnspan=2,
                            row=3, 
                            padx=(10, 250))  
            self.input_check = 0
            
        if CheckingInput.invalid == 3:
            self.err_4 = Label(self, text="You must be in\nYear 1 to Year 6.", fg="red", bg="#f0f0f0", width=18)
            self.err_4.grid(column=2, row=3, columnspan=2, padx=(10,250))
            self.input_check = 0 

        if CheckingInput.invalid == 4:
            self.err_5 = Label(self, text="Choose your\ndifficulty level!", fg='red', bg='#f0f0f0')
            self.err_5.grid(column=2, row=6,
                            columnspan=2,
                            padx=(10,150))

        if self.sn.get() == '' or self.sn.get() == 'Tell us your name!':
            self.err_1 = Label(self, text="Fill in your name!", fg="red", bg="#f0f0f0")
            self.err_1.grid(column=0, columnspan=2,
                       row=3, 
                       padx=(200,0))
            self.input_check = 0
    
        if self.yr.get() == '' or self.yr.get() == 'Your year level?':
            self.err_2 = Label(self, text="Fill in your year level!", fg="red", bg="#f0f0f0")
            self.err_2.grid(column=2, row=3,
                            columnspan=2,
                            padx=(10,250)
                            )
            self.input_check = 0

        if self.input_check == 0:
            CheckingInput.check = []
        elif self.input_check == 1 and CheckingInput.invalid == 0:
            self.store_info()
    
    def send_info(self):
        self.object = CheckingInput()
        if len(CheckingInput.check) == 0:
            CheckingInput.check.extend([self.sn.get(), self.yr.get(), self.diff_lvl])
            print('Step 1: Checking list', CheckingInput.check)
            self.object.input_check()
            self.errors()
            return True
        elif len(CheckingInput.check) < 3:
            CheckingInput.check.extend([self.sn.get(), self.yr.get(), self.diff_lvl])
            self.object.input_check()
            self.errors()
        elif len(CheckingInput.check) > 3: 
            Label(self, text="Unknown error. Please exit programme and reopen it.", 
                  fg="red").grid(column=0, row=1)
            Student.attr_list = []
            return False
           
    def conf_message(self, a):
        #Confirmation message pops up when user chooses difficulty level
        Label(self, text=f"You've chosen\n{a} mode!", 
              borderwidth=2, 
              background="orange",
              width=10,
              height=2).grid(column=2, columnspan=2,
                                        row=6, 
                                        ipadx=10,
                                        padx=(10,150))

    def choose_diff(self):
        if self.diff_value.get() == 101:
            self.conf_message("EASY")
            self.diff_lvl = "Easy"
        elif self.diff_value.get() == 102:
            self.conf_message("MEDIUM")
            self.diff_lvl = "Kinda easy"
        elif self.diff_value.get() == 103:
            self.conf_message("HARD")
            self.diff_lvl = "Not so easy"
        return self.diff_lvl

    def reset(self):
        self.name_input.delete(0, 'end')
        self.difficulty = None
