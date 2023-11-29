"""
Jennifer Larsen
11/8/2023
This program creates a person class and a student class and displays the results.
"""
import gc


class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()


class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def display(self):
        return f"{self.street}\n{self.city}, {self.state} {self.zip_code}"


class Student:
    def __init__(self, person, major, start_date, gpa):
        self.person = person
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return f"Student Information:\n{self.person.display()}\nMajor: {self.major}\nStart Date: {self.start_date}\nGPA: {self.gpa}"


def main():
    # Create a person object
    person = Person("Larsen", "Jennifer", Address("123 Main St", "Anytown", "IA", "12345"))

    # Create a student object
    student = Student(person, "Computer Information Systems", "2023-1-01", 4.0)

    # Display the student
    print("Initial Student Information:")
    print(student.display())

    # Change the major
    student.change_major("Being Awesome!")

    # Update the GPA
    student.update_gpa(3.0)

    # Display the updated student information
    print("\nUpdated Student Information:")
    print(student.display())

    # Perform garbage collection (not necessary in Python, but included as a step)
    gc.collect()


if __name__ == "__main__":
    main()
