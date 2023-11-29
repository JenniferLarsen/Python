"""
Jennifer Larsen
11/8/2023
This program creates a person class and a student class that inherits from person and displays the results.
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Student(Person):
    """Derived Student class from Person"""
    def __init__(self, student_id, lname, fname, major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self._major = major
        self._gpa = gpa
        self._student_id = student_id

    def display(self):
        return super().display() + f":({self._student_id}) {self._major} gpa: {self._gpa}"


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())

my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())

my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
