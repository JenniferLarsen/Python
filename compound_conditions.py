"""
Program: compound_conditions.py
Author: Jennifer Larsen
Last date modified: 09/12/2023
The purpose of this program is to demonstrate compound conditions.
The input is a max and min number.
The output is the results of conditions placed upon the max and min number.
"""

"""Open your Python shell, PyCharm, or Jupyter Notebook, and test making expressions.

Set MAX = 10, MIN = 0
Set a variable y to a value 
Test whether y is above MAX
Test whether y is below MIN
Set a variable x to a value
Test whether it is between the MIN and MAX but does not equal MAX nor MIN
Test whether it is within MIN up to MAX but does not equal MAX  
Test whether it is above MIN up to and including MAX"""

MAX = 10 
MIN = 0
y = 22
print(y > MAX)
print(y < MIN)

x = 7
print(MAX > 7 > MIN)
print(MAX > 7 >= MIN)
print(MIN < 7 <= MAX)

print(f"x = {x}, y = {y}, MAX = {MAX}, MIN = {MIN}")
