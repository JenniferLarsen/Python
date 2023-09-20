"""
Program: paramater_return_value.py
Author: Jennifer Larsen
Last date modified: 09/19/2023
The purpose of this program is to multiply an input string.
    :param name, string, number as int
    :returns the string multiplied by the int
"""
def multiply_string(phrase: str, number: int):
    if not isinstance(phrase, str):
        raise ValueError("phrase must be a string")
    if not isinstance(number, int) or number <= 0:
        raise ValueError("number must be a positive integer")

    multiplied_string = phrase * number
    return multiplied_string

if __name__ == '__main__':
    try:
        result = multiply_string('Python!', 4)
        print(result)
    except ValueError:
        print(f"Please enter a string and an integer.")