from tkinter import *

class Student:
    attr_list = []  #List variable to append info as programme runs
    invalid = 0
    #Declare retry variable at the student class
    #Student class does not restart even if player chooses retry
    retry_times = 0
    def __init__ (self, sn, yr, lvl, scr):
        self.student_name = sn
        self.year_level = yr
        self.diff_lvl = lvl
        self.score = scr

    def input_check(self):
        #Assuming info has been stoed into attr_list list
        if len(Student.attr_list) == 3: #3 attr of name, year and diff lvl
            self.name = Student.attr_list[0]
            self.year = Student.attr_list[1]
            self.diff = Student.attr_list[2]
            #Invalid checking
            try:
                sy_number = int(self.year)
                return sy_number, True
            except ValueError: #player used text instead of number for year lvl
                Student.invalid = 2 
                ''' 2 = text instead of num '''
            
            #Boundaries for year lvl
            if self.scr < 1 or self.scr > 6: #Can only be students year 1-6
                Student.invalid = 3
                ''' 3 = invalid year level - boundaries '''
            return True

        elif len(Student.attr_list) < 3: #BLANKS - user did not input  info
            Student.invalid = 1 
            ''' 1 = all / some fields are blank -- return to interface to give error'''
            return False
        
        
    def class_obj(self):
        #Data encapsulation as soon as when final frame initiates - all attributes contain info
        '''     All data checking must have occured before this!    '''
        self.student = Student(self.student_name, self.year_level, self.diff_lvl, self.score)
        #Print self.student object as a string. Code ref: https://www.educative.io/edpresso/what-is-the-str-method-in-python
        print(self.student.__str__())

    def write_file(self):
        #No divider in the write text file to append additional info of later attempts
        with open("students.txt", 'a', encoding = 'utf-8') as f: #file always closes even when operations unexpectedly fail
            f.write(f"===========\nStudent's name: {self.student_name}\nDifficulty level: {self.diff_lvl}\nStudent's score: {self.score}\n")


    '''def retry(self):
        #New score will become the score in the object's attribute scr
        #However old score will not be erased from file
        #New score is added with title "Second attempt"
        #Code ref: https://www.programiz.com/python-programming/methods/list/pop 
        Student.write_file(self.student)
        self.retry_count = Student.retry_times
        self.retry_count = self.retry_count + 1
        self.score_2 = Student.attr_list.pop(3) #replaces student's old score with new one in instance
        print(self.score_2)
        print(len(Student.attr_list))
        if len(Student.attr_list) == 4:
            with open("students.txt", 'a', encoding = 'utf-8') as f: #file always closes even when operations unexpectedly fail
                f.write(f"Attempt {self.retry_count}: {self.score}")
    
    def new_player(self):
        #Only write to file if click new player
        Student.write_file(self.student)
        with open("students.txt", 'a', encoding = 'utf-8') as f: #file always closes even when operations unexpectedly fail
            f.write(f"===========\n\n")'''
