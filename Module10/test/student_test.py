import unittest
from class_definitions import student as s

"""
Jennifer Larsen
10/30/2023
This program explores writing and using Classes and Tests
"""


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Duck', 'Daisy', 'French', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        student = s.Student("Duck", "Donald", "Engineering")
        self.assertEqual(student.last_name, "Duck")
        self.assertEqual(student.first_name, "Donald")
        self.assertEqual(student.major, "Engineering")
        self.assertEqual(student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        student = s.Student("Mouse", "Mickey", "Computer Science", 3.5)
        self.assertEqual(student.last_name, "Mouse")
        self.assertEqual(student.first_name, "Mickey")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 3.5)

    def test_student_str(self):
        student = s.Student("Duck", "Donald", "Engineering", 2.8)
        expected_str = "Duck, Donald has major Engineering with gpa: 2.8"
        self.assertEqual(str(student), expected_str)

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = s.Student("", "Mickey", "Computer Science", 3.5)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            student = s.Student("Mouse", "", "Computer Science", 3.5)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = s.Student("Mouse", "Mickey", "", 3.5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = s.Student("Duck", "Donald", "Engineering", -1.0)


if __name__ == '__main__':
    unittest.main()
