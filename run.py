#!/usr/bin/env pythonf
from student import Student
from teacher import Teacher

gradelevels = ["kindergarten","grade1","grade2","grade3","grade4","grade5","grade6","grade7","grade8","grade9","grade10","grade11","grade12"]
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
        # print "Your school is: " + school
        print "\n gradelevels in your school:"
        for gradeLevel in gradelevels:
             print str(counter) + "." + gradeLevel
             counter +=1
        selected_grade = raw_input("type  a number that corresponds to  your gradeLevel, eg type 2 to select g2:  ")
        selected_grade = int(selected_grade)
        my_grade = gradelevels[selected_grade -1]
        print "You selected grade: " + my_grade
        print "\nAre you a"
        print " 1.Teacher \n    or \n 2. Student??"

    option = raw_input("Type 1 if you are a teacher or type 2 if you are a student:  ")
    if option =="1":
        create_a_teacher("sf","sdffese",my_grade)
    elif option == "2":
        pass
    else:
        print "Please enter a valid option"

def create_a_teacher(fName,sname,gradeLevel):
    teacher= Teacher()
    teacher.setfName(fName)
    teacher.setsName(sname )
    teacher.setgradeLevel(gradeLevel)

    teachers.append(teacher_object)

    for teacher in teachers:
        print teacher.getfName()
        print teacher.getgradeLevel()


main()
