"""
Jennifer Larsen
10/25/2023
This program creates a basic GUI for a selecting a user's favorite meal.
"""


import tkinter as tk


def on_checkbutton_click():
    label_waiting.config(text="Enjoy your meal!")


root = tk.Tk()


root.title("Favorite Meal")


check_buttons = []
for i, meal in enumerate(["Breakfast", "Second Breakfast", "Lunch", "Dinner"]):
    checkbutton = tk.Checkbutton(root, text=meal, command=on_checkbutton_click)
    checkbutton.grid(row=i, column=0, sticky="w")
    check_buttons.append(checkbutton)


label_waiting = tk.Label(root, text="Waiting")
label_waiting.grid(row=4, column=0)


exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=5, column=0)


root.mainloop()

