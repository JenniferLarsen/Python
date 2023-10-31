"""
Jennifer Larsen
10/30/2023
This program explores writing and using Classes and Tests
"""


class Student:

    def __init__(self, lname, fname, major, gpa=0.0):
        if not lname or not fname or not major:
            raise ValueError("Empty value for last_name, first_name, or major")
        if not isinstance(gpa, float) or gpa < 0.0 or gpa > 4.0:
            raise ValueError("Invalid GPA value")
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


if __name__ == '__main__':
    # Create two student objects
    student1 = Student("Duck", "Donald", "Engineering", 3.5)
    student2 = Student("Mouse", "Mickey", "Computer Science", 2.8)

    # Print the student objects
    print(student1)
    print(student2)
