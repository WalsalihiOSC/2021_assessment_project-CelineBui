from tkinter import *

class Student:
    def __init__ (self, sn, lvl):
        self.student_name = sn
        self.diff_lvl = lvl

    def store_info(self):
        with open("students.txt") as f: #file always closes even when operations unexpectedly fail
            f.write(f"===========\n Students name: {self.student_name}\n \
                Difficulty level: {self.diff_lvl}\n ===========\n \n")