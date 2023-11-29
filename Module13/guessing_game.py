"""
Jennifer Larsen
11/22/2023
This program creates a simple GUI number guessing game and unit test.
"""


import tkinter as tk
from tkinter import messagebox
from number_guesser import NumberGuesser
import random


class NumberGuessingGame:
    def __init__(self, root, max_value):
        self.root = root
        self.max_value = max_value
        self.target_number = None
        self.guess_entry = None
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Create Start Game button
        start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.pack()

        # Create guess entry
        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        # Create number buttons
        for i in range(1, self.max_value + 1):
            button = tk.Button(self.root, text=str(i), state=tk.DISABLED, command=lambda num=i: self.make_guess(num))
            self.buttons.append(button)
            button.pack()

    def start_game(self):
        self.target_number = random.randint(1, self.max_value)
        for button in self.buttons:
            button.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)

    def make_guess(self, guess):
        if guess == self.target_number:
            messagebox.showinfo("Winner", "Congratulations! You guessed the correct number.")
            self.reset_game()
        else:
            self.buttons[guess - 1].config(state=tk.DISABLED)
            NumberGuesser.add_guess(guess)

    def reset_game(self):
        self.target_number = None
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        self.guess_entry.delete(0, tk.END)
        NumberGuesser.guessed_list = []


if __name__ == '__main__':
    root = tk.Tk()
    game = NumberGuessingGame(root, max_value=10)
    root.mainloop()
