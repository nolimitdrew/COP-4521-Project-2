# Andrew Stade
# 1/29/2021
# afs18c
# The program in this file is the individual work of Andrew Stade.

import math

class Student:
    firstName=""
    lastName=""
    gender=""
    level=""
    gpa=""
    def __init__(my, firstName="", lastName="", gender="", level="", gpa=""):
        if(gender.lower() != "m" and gender.lower() != "f" and gender.lower() != "male" and gender.lower() != "female"):
            print("Gender Error")
        elif(level.lower() != "freshman" and level.lower() != "sophomore" and level.lower() != "junior" and level.lower() != "senior"):
            print("Class Error")
        else:
            my.firstName = firstName
            my.lastName = lastName
            my.gender = gender
            my.level = level
            my.gpa = gpa
            
        if(float(my.gpa)>4):
            my.gpa=4
            
    def show_myself(my):
        print("First Name: " + my.firstName)
        print("Last Name: " + my.lastName)
        print("Gender: " + my.gender)
        print("Class Level: " + my.level)
        print("GPA: " + str(my.gpa))
        
    def study_time(my,st):
        gp = float(my.gpa) + math.log10(st)
        my.gpa = gp
        if(float(my.gpa)>4):
            my.gpa=4
s1 = Student("Mike", "Barnes", "Male", "Freshman", 4)
s2 = Student("Jim", "Nickerson", "Male", "Sophomore", 3)
s3 = Student("Jack", "Indabox", "Male", "Junior", 2.5)
s4 = Student("Jane", "Miller", "Female", "Senior", 3.6)
s5 = Student("Mary", "Scott", "Female", "Senior", 2.7)

student_list = [s1,s2,s3,s4,s5]

for i in student_list:
    i.show_myself()
    i.study_time(5)
    i.show_myself()