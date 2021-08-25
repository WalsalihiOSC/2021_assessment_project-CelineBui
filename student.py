from tkinter import *

class Student:
    attr_list = []
    
    def __init__ (self, sn, yr, lvl, scr):
        self.student_name = sn
        self.year_level = yr
        self.diff_lvl = lvl
        self.score = scr


    def __str__(self) -> str:
        with open("students.txt") as f: #file always closes even when operations unexpectedly fail
            f.write(f"===========\n Student's name: {self.student_name}\n \
                Difficulty level: {self.diff_lvl}\n \
                Student's score: {self.score}\n ===========\n \n")
        #String representation of an object - object is created with associate attributes
        return f'({self.student_name}, {self.diff_lvl}, {self.score})'
        
    #from welcome_window import welcome_win 
    '''welcome_win contains variables with values for name and diff levels 
    to be associated with each instance/object of the Student class'''
    #students = []
    #students.append(Student(self.sn, self.diff_lvl, self.scr))
    '''
    self.sn contains student's name input
    self.diff_lvl contains student's chosen diff lvl
    self.scr contains student's scores
    '''
    #this is to avoid having to manually call new variables for new instance
