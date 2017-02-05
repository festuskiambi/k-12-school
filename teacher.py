from collections import defaultdict
class Teacher(object):
    def __init__(self):

        #class variables
        self.first_ame=None
        self.sur_name=None
        self.gradeLevel=None
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
    #get school
    def get_school(self):
        return self.school
    #set school
    def set_school(self,school):
        self.school = school
