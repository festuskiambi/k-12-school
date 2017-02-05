class Student(object):
    def __init__(self):
        self.first_name=None
        self.sur_name=None
        self.gradeLevel=None
        self.gpa=None
        self.teacher=None
        self.school=None
    #get first_name
    def get_first_name(self):
        return self.first_name
    #set first_name
    def set_first_name(self,first_name):
        self.first_name = first_name
    #get sur_name
    def get_sur_name(self):
        return self.sur_name
    #set sur_name
    def set_sur_name(self,sur_name):
        self.sur_name = sur_name
    #get gradeLevel
    def get_gradeLevel(self):
        return self.gradeLevel
    #set gradeLevel
    def set_gradeLevel(self,gradeLevel):
        self.gradeLevel = gradeLevel
    #set gpa
    def get_gpa(self):
        return self.gpa
    #set gpa
    def set_gpa(self,gpa):
        self.gpa = gpa
    #get teacher
    def get_teacher(self):
        return self.teacher
    #set teacher
    def set_teacher(self,teacher):
        self.teacher = teacher
    #get school
    def get_school(self):
        return self.school
    #set school
    def set_school(self,school):
        self.school = school
