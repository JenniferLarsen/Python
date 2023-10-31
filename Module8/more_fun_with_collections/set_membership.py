"""
Jennifer Larsen
10/17/2023
set_membership.py
This code takes in an input_set and a value and checks if the value is in the set
Then returns output indicating if the value is or is not in the set.
"""

def in_set(input_set, value):
    return value in input_set


def main():
    test_set = {'banana', 'apple', 'cherry'}
    test_value1 = 'apple'
    test_value2 = '5'
    if in_set(test_set, test_value1):
        print(f"The value '{test_value1}' is in the set {test_set}")
    else:
        print(f"The value '{test_value1}' is not in the set {test_set}")

    if in_set(test_set, test_value2):
        print(f"The value '{test_value2}' is in the set {test_set}")
    else:
        print(f"The value '{test_value2}' is not in the set {test_set}")


if __name__ == "__main__":
    main()






