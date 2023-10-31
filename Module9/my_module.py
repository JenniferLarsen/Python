"""
Jennifer Larsen
10/25/2023
This program uses modules to display set greetings, authors, dictionaries and sets.
"""
import my_definitions as md


foods_dict = {"Fruit": "Mango", "Protein": "Steak", "Veggie": "Spinach", "Dairy": "Cheese"}
course1 = ["French", "Monday and Wednesday", "A"]
course2 = ["Python", "Online only", "A"]
course3 = ["Html/Css", "Online only", "A"]
course_set = (course1, course2, course3)

if __name__ == '__main__':
    md.greeting()
    md.message()
    md.print_dict(foods_dict)
    md.print_set(course_set)
