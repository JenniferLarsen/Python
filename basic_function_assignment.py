"""
Program: basic_function_assignment.py
Author: Jennifer Larsen
Last date modified: 09/18/2023
The purpose of this program is to use a function called hourly_employee_input that asks the user for a name (string), 
hours worked (int) and an hourly pay rate (float) and prints a string including the information. 
The input is an integer representing hours worked, and a float representing the hourly pay rate. 
The output is a summary of the input with the name, hours worked, hourly pay rate and total pay.
"""

def hourly_employee_input(name: str, hours_worked: int, hourly_pay_rate: float):
    try:
        if int(hours_worked) < 0 or float(hourly_pay_rate) < 0:
            raise ValueError("Hours worked and Hourly pay rate must be positive numbers.")
        else:
            total_pay =int(hours_worked) * float(hourly_pay_rate)
            return(f'{name} worked {hours_worked} hours at ${hourly_pay_rate :.2f} per hour, for a total of ${total_pay :.2f}.')
    except ValueError:
        print("Hours worked and Hourly pay rate must be positive numbers.")
    except TypeError:
        print("Hours worked and Hourly pay rate must be positive numbers.")

def weekly_pay(hours_worked: float, hourly_pay_rate: float): 
    weekly_pay = hours_worked * hourly_pay_rate
    return(weekly_pay)

if __name__ == '__main__':
    try:  # check for ValueError
        display_string = hourly_employee_input()  # function call, store in a variable
    except ValueError as err:
        print("ValueError encountered! ")
    else:
        print(display_string)  # print the result of the function
hourly_employee_input('Jennifer', 40, 35.00)

hourly_employee_input('Jennifer', -40, -35.00)

hourly_employee_input(22, 'J', 'L')
