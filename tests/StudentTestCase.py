"""
Program: StudentTestCase.py
Author: Tony Ehlert
Last date modified: 3/24/2023

The purpose of this program is to test the Student class
The input is tests and necessary variables to test the Student class
The output is results of the tests
"""
import unittest

from class_definitions import Student


class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student("Stark", "Tony", "Computer Science")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        """
        Test constructor values set to only required attributes for acceptable values
        """
        self.assertEqual(self.student.last_name, "Stark")
        self.assertEqual(self.student.first_name, "Tony")
        self.assertEqual(self.student.major, "Computer Science")

    def test_object_created_all_attributes(self):
        """
        Test constructor values set to all attributes for acceptable values
        """
        student = Student("Stark", "Tony", "Computer Science", 3.0)
        self.assertEqual(student.last_name, "Stark")
        self.assertEqual(student.first_name, "Tony")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 3.0)

    def test_student_str(self):
        """
        Test the str() method, (in rubric this is display())
        """
        self.assertEqual(self.student.__str__(), "Stark, Tony has major Computer Science with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        """
        Tests that expect exception raised, Add exception to constructor (not in test!)
        """
        with self.assertRaises(ValueError):
            student = Student("123", "Tony", "Computer Science")

    def test_object_not_created_error_first_name(self):
        """
        Add exception to constructor (not in test!)
        """
        with self.assertRaises(ValueError):
            student = Student("Stark", "123", "Computer Science")

        # def test_object_not_created_error_last_name(self):
        """
        Add exception to constructor
        """
        # self.assertEquals(0, 1)

    def test_object_not_created_error_major(self):
        """
        Add exception to constructor
        """
        with self.assertRaises(ValueError):
            student = Student("Stark", "Tony", "CIS 189")

    def test_object_not_created_error_gpa(self):
        """
        Add exception to constructor
        NOTE: look up how isinstance(gpa, float) works AND check range
        """
        with self.assertRaises(ValueError):
            student = Student("Stark", "Tony", "Computer Science", "abc")
        with self.assertRaises(ValueError):
            student = Student("Stark", "Tony", "Computer Science", 4.1)

    # creation of two student objects and printout of them
    student1 = Student("Stark", "Tony", "Computer Science")
    student2 = Student("Rodgers", "Steve", "Music Education", 4.0)

    print(student1)
    print(student2)

    del student1
    del student2


# Driver/ main()
if __name__ == "__main__":
    StudentTestCase.main()
