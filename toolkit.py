"""
Program: toolkit.py
Author: Jennifer Larsen
Last date modified: 09/12/2023
The purpose of this program is to take user input and output price of selected subscription.
The input is a string representing the user's subscription selection.
The output is the subscription level selected and the price.
"""

print("Welcome to the Programmer's Toolkit Monthly Subscription Box! Each month is something different, t-shirts, stickers, figurines, even programming books!")
user_selection = input("Please enter your subscription level(Platinum, Gold, Silver, Bronze, Free Trial): ")

if user_selection == "Platinum":
    print("Platinum subscription is $60 per month.")
elif user_selection == "Gold":
    print("Gold subscription is $50 per month.")
elif user_selection == "Silver":
    print("Silver subscription is $40 per month.")
elif user_selection == "Bronze":
    print("Bronze subscription is $30 per month.")
else:
    print("Free Trial is Free.")


"""Manual Test Cases:
       Input            Expected Output                             Actual Output
1. Platinum   Platinum subscription is $60 per month.           Platinum subscription is $60 per month.
2. Gold         Gold subscription is $50 per month.                 Gold subscription is $50 per month.
3. Silver       Silver subscription is $40 per month.           Silver subscription is $40 per month.
4. Bronze       Bronze subscription is $30 per month.           Bronze subscription is $30 per month.
5. Free Trial   Free Trial is Free.                             Free Trial is Free.
"""