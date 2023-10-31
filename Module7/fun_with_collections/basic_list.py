"""
basic_list.py
Jennifer Larsen
10/9/2023
This module contains functions to explore basic lists
"""


def get_input():
    user_input = input("Please enter a number: ")
    return user_input


def make_list(num):
    my_list = []
    for i in range(num):
        user_input = get_input()
        try:
            my_list.append(int(user_input))
        except ValueError:
            raise ValueError("Invalid input. Please enter an integer.")
    return my_list


if __name__ == "__main__":
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))
