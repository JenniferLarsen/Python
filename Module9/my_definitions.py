"""
Jennifer Larsen
10/25/2023
This program uses modules to display set greetings, authors, dictionaries and sets.
"""


def greeting():
    greet = "Hello! I hope you have a great day!"
    print(greet)


def message():
    auth = "Author is Jennifer Larsen"
    print(auth)


def print_dict(input_dict):
    for key, value in input_dict.items():
        print(f"{key}: {value}")


def print_set(input_set):
    for item in input_set:
        print(item)
