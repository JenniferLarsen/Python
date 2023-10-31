"""
Jennifer Larsen
10/25/2023
This program uses packages and modules to display set greetings, authors, dictionaries and sets.
"""


import definitions.dictionary_ops, definitions.set_ops, definitions.greeting


foods_dict = {"Fruit": "Mango", "Protein": "Steak", "Veggie": "Spinach", "Dairy": "Cheese"}

course1 = ["French", "Monday and Wednesday", "A"]
course2 = ["Python", "Online only", "A"]
course3 = ["Html/Css", "Online only", "A"]

course_set = (course1, course2, course3)

if __name__ == '__main__':

    definitions.greeting.greeting()
    definitions.greeting.message()
    definitions.dictionary_ops.print_dict(foods_dict)
    definitions.set_ops.print_set(course_set)


