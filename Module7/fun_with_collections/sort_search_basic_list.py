"""
sort_search_basic_list.py
Jennifer Larsen
10/9/2023
This module contains functions to explore basic lists and adds search and sort functions
to previous basic_list.py assignment.
"""
import basic_list


def get_input() -> str:
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


def sort_list(my_list):
    sorted_list = sorted(my_list)
    return sorted_list
# Return statements in these functions provide results back to the caller, enabling modularity
# and making it easier to work with the data they produce.


def search_list(my_list, value):
    try:
        return my_list.index(value)
    except ValueError:
        return -1
# Return statements in these functions provide results back to the caller, enabling modularity
# and making it easier to work with the data they produce.


if __name__ == "__main__":
    my_list = make_list(3)  # Call make_list() once to get a list of 3 numbers
    print(my_list)

    sorted_list = sort_list(my_list)  # Sort the list
    print(sorted_list)  # Print sorted list

    # Search for the value 3 in the list.
    index = search_list(sorted_list, 3)
    if index != -1:
        print("The value 3 is at index", index)
    else:
        print("The value 3 is not in the list.")
