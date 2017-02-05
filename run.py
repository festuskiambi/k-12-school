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
        selected_grade = raw_input("\n enter  a number that corresponds to  a gradeLevel, eg type 2 to select grade1:  ")
        selected_grade = int(selected_grade)
        my_grade = gradelevels[selected_grade -1]
        print "You selected grade is: " + my_grade

         #check the teachers in the selected grade
        teacher = Teacher()
        if not teachers:
            print "\nthere are no teachers in " +my_grade
            print "\ndo you want to add a teacher \n"
            print " 1. Yes \n    or \n 2. No"
            option = raw_input("\n Type 1 if you want to add a teacher or type 2 to exit  ")
            if option =="1":
                print "\nYou are adding a  teacher\n"
                first_name = raw_input("Enter teacher's first name: ")
                sur_name= raw_input("\nEnter teacher's sur name: ")
                create_a_teacher(first_name,sur_name,my_grade,school)
                teacher_name = first_name + "  " + sur_name
                print "Do you want to add students to " + teacher_name  +"?"
                print " 1. Yes \n    or \n 2. No"
                option = raw_input("\n Type 1 if you want to add a students or type 2 to exit  ")
                if option =="1":
                    print "\nYou are adding a  student\n"
                    no_of_students = len(students)
                    while no_of_students<=10:
                        first_name = raw_input("\nEnter student's first name: ")
                        sur_name= raw_input("Enter  student's sur name: ")
                        gpa = raw_input("Enter  student's gpa: ")

                        create_a_student(first_name,sur_name,my_grade,gpa,teacher_name,school)
                        no_of_students+=1
                elif  option == "2":
                    exit()


            elif option == "2":
                exit()

#a function to create a teacher
def create_a_teacher(first_name,sur_name,gradeLevel,school):
    teacher= Teacher()
    teacher.set_first_name(first_name)
    teacher.set_sur_name(sur_name )
    teacher.set_gradeLevel(gradeLevel)
    teacher.set_school(school)
    teachers.append(teacher)
# a function to create a teacher
def create_a_student(first_name,sur_name,gradeLevel,gpa,teacher,school):
    student = Student()
    student.set_first_name(first_name)
    student.set_sur_name(sur_name)
    student.set_gradeLevel(gradeLevel)
    student.set_gpa(gpa)
    student.set_school(school)
    students.append(student)
if __name__ == "__main__":
    main()
