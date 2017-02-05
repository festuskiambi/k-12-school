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

        print "\n Gradelevels at " + school + ":\n"
        for gradeLevel in gradelevels:
             print str(counter) + "." + gradeLevel
             counter +=1
        selected_grade = raw_input("\n type  a number that corresponds to  your gradeLevel, eg type 2 to select grade1:  ")
        selected_grade = int(selected_grade)
        my_grade = gradelevels[selected_grade -1]
        print "You selected grade is: " + my_grade
        print "\nAre you a"
        print " \n1.Teacher \n    or \n 2. Student?"

    option = raw_input("\n Type 1 if you are a teacher or type 2 if you are a student:  ")
    if option =="1":
        print "You are a teacher\n"
        first_name = raw_input("Enter your first name:")
        sur_name= raw_input("\nEnter your sur name:")
        create_a_teacher(first_name,sur_name,my_grade,school)

    elif option == "2":
        pass
    else:
        print "Please enter a valid option"

def create_a_teacher(first_name,sur_name,gradeLevel,school):
    teacher= Teacher()
    teacher.set_first_name(first_name)
    teacher.set_sur_name(sur_name )
    teacher.set_gradeLevel(gradeLevel)
    teacher.set_school(school)
    teachers.append(teacher)


    for teacher in teachers:
        print teacher.get_first_name()
        print teacher.get_gradeLevel()
        print teacher.get_school()



main()
