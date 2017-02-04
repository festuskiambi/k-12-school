#!/usr/bin/env python
gradelevels = ["k","g1","g2","g3","g4","g5","g6","g7","g8","g9","g10","g11","g12"]
students = []
teachers = []
school = ""

def main():
    school = raw_input("Enter the name of your school:  \n")
    counter = 1
    if school=="":
        print "Please enter your school name"
        school = raw_input("Enter the name of your school:  \n")
    else:
        print "Your school is: " + school
        print "\n gradelevels in your school:"
        for gradeLevel in gradelevels:
             print str(counter) + "." + gradeLevel
             counter +=1
        selected_grade = raw_input("type  a number that corresponds to  your gradeLevel, eg type 2 to select g2:")
        selected_grade = int(selected_grade)
        my_grade = gradelevels[selected_grade -1]
        print my_grade



        print "1. Student?\n"
        print "2. Teacher?"
    option = raw_input("Type 1 if you are a student or type 2 if you are a teacher: \n")




main()
