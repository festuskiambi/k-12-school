#!/usr/bin/env pythonf
import pickle
from student import Student
from teacher import Teacher


gradelevels = ["kindergarten","grade1","grade2","grade3","grade4","grade5","grade6","grade7","grade8","grade9","grade10","grade11","grade12"]
students = []
teachers = []
school = ""


def main():

    school = raw_input("Enter the name of your school:  \n")
    counter = 1
    count = 1
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
        print "\nAre you a\n"
        print " 1.Teacher \n    or \n 2. Student?"

    option = raw_input("\n Type 1 if you are a teacher or type 2 if you are a student:  ")
    if option =="1":
        print "\nYou are a teacher\n"
        first_name = raw_input("Enter your first name: ")
        sur_name= raw_input("\nEnter your sur name: ")
        create_a_teacher(first_name,sur_name,my_grade,school)
        main()

    elif option == "2":
        teacher = Teacher()
        print "\nYou are a student\n"
        #check if there teachers in
        if not teachers:
            print "there are no teachers in your school try again later "
            exit()
        else:
            for teacher in teachers:

                if  teacher.get_gradeLevel() ==my_grade:
                    print "these are the teachers in your grade:"
                    print str(counter) + teacher.get_first_name ()+ "  " + teacher.get_sur_name()
                    count +=1
                    my_teacher = raw_input("\n enter the name of your teacher from the list shown obove  ")
                else:
                    print "there no teachers in your grade"


            for student in students:
                print student.get_gradeLevel()


        first_name = raw_input("Enter your first name: ")
        sur_name= raw_input("Enter your sur name: ")
        gpa = raw_input("\nEnter your gpa: ")

        create_a_student(first_name,sur_name,my_grade,gpa,my_teacher,school)

    else:
        print "Please enter a valid option"

def create_a_teacher(first_name,sur_name,gradeLevel,school):
    teacher= Teacher()
    teacher.set_first_name(first_name)
    teacher.set_sur_name(sur_name )
    teacher.set_gradeLevel(gradeLevel)
    teacher.set_school(school)
    teachers.append(teacher)




def create_a_student(first_name,sur_name,gradeLevel,gpa,teacher,school):
    student = Student()
    student.set_first_name(first_name)
    student.set_sur_name(sur_name)
    student.set_gradeLevel(gradeLevel)
    student.set_gpa(gpa)
    student.set_school(school)
    students.append(student)







main()
