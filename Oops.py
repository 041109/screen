import pygame

class Student:
    name = "Ryan"
    age = 14
    age=str(age)
    schoolclass = "9KFD"
    classteacher = "Miss Priya"
    
    def __init__(self):
        print("making a new student")

    # another function

    def show_details(self):
        print(f"The details of the student are: ")
        print(f"Name: {self.name} ")
        print(f"Age: {self.age} ")
        print(f"Class: {self.schoolclass} ")
        print(f"Teacher: {self.classteacher} ")

 # print( "Age of student is " + Student.age)
print( " Your class teacher is " + Student.classteacher)

print(f"Age of student: {Student.age} years")

# object 1 
student1 = Student()
student1.show_details()