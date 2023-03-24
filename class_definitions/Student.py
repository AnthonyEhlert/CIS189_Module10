"""
Program: Student.py
Author: Tony Ehlert
Last date modified: 3/24/2023

The purpose of this program is to define a Student class and its methods
The input is constructor method and helper methods
The output is print to the console of the data of the object using the __str__() method
"""
class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        # supersets for validation
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")

        # if statements against supersets for validation
        if not (name_characters.issuperset(lname)):
            raise ValueError
        if not (name_characters.issuperset(fname)):
            raise ValueError
        if not (major_characters.issuperset(major)):
            raise ValueError

        # check if gpa is float and within acceptable range
        if not (isinstance(gpa, float)):
            raise ValueError
        if (gpa < 0.0 or gpa > 4.0):
            raise ValueError


        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

if __name__ == "__main__":
    student1 = Student("Stark", "Tony", "Computer Science", 4.0)
    print(student1)

    student2 = Student("Rodgers", "Steve", "History")
    print(student2)

    del student1
    del student2
