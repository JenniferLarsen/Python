"""
Jennifer Larsen
11/22/2023
This program creates a simple GUI number guessing game and unit test.
"""


class NumberGuesser:
    guessed_list = []

    @classmethod
    def add_guess(cls, guess):
        cls.guessed_list.append(guess)
