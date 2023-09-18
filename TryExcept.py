"""
Program: TryExcept.py
Author: Jennifer Larsen
Last date modified: 09/16/2023
The purpose of this program is to take user input and calculate
the average of 4 test scores with input validation.
The input is an integer representing the user's name, age, four integers representing
the four test scores.
The output is a summary of the input with the average test score and any errors that occurred.
"""

#Ask user their name, age and test scores
NUM_OF_TEST_SCORES = 4
first_name = str(input("Please enter your First name:"))
last_name = str(input("Please enter your Last name:"))
try:
    user_age = int(input("Please enter your age: "))  
    if not (6 <= user_age <= 122):  
        print("Please enter a valid age between 6 and 122")
        user_age = int(input("Please enter your age: "))  
except ValueError:
    print("Please enter a valid age as a number")  
    user_age = int(input("Please enter your age: "))

try:
    first_test = int(input("Please enter the first test score:"))
    if not (0 <= first_test <= 100):
        print("Please enter a valid test score between 0 and 100:")
        first_test = int(input("Please enter the first test score:"))
except ValueError:
    print("Please enter a valid test score as a number between 0 and 100: ")
    first_test = int(input("Please enter the first test score:"))

try: 
    second_test = int(input("Please enter the second test score:"))
    if not (0 <= second_test <= 100):
        print("Please enter a valid test score between 0 and 100:")
        second_test = int(input("Please enter the second test score:"))
except ValueError:
    print("Please enter a valid test score as a number between 0 and 100: ")
    second_test = int(input("Please enter the second test score:"))

try:
    third_test = int(input("Please enter the third test score:"))
    if not (0 <= third_test <= 100):
        print("Please enter a valid test score between 0 and 100:")
        third_test = int(input("Please enter the third test score:"))
except ValueError:
    print("Please enter a valid test score as a number between 0 and 100: ")
    third_test = int(input("Please enter the third test score:"))

try:
    fourth_test = int(input("Please enter the fourth test score:"))
    if not (0 <= fourth_test <= 100):
        print("Please enter a valid test score between 0 and 100:")
        fourth_test = int(input("Please enter the fourth test score:"))
except ValueError:
    print("Please enter a valid test score as a number between 0 and 100: ")
    fourth_test = int(input("Please enter the fourth test score:"))

average_score = (first_test + second_test + third_test + fourth_test)/NUM_OF_TEST_SCORES

print(f"{last_name}, {first_name}  Age: {user_age}. Your average test score is {average_score:.2f}.")



