"""
Jennifer Larsen
11/22/2023
This program creates a simple GUI number guessing game and unit test.
"""


import unittest
from number_guesser import NumberGuesser


class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        NumberGuesser.guessed_list = []

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(NumberGuesser.guessed_list, [])

    def test_adding_to_guessed_list(self):
        NumberGuesser.add_guess(5)
        self.assertEqual(NumberGuesser.guessed_list, [5])

        NumberGuesser.add_guess(8)
        self.assertEqual(NumberGuesser.guessed_list, [5, 8])

        NumberGuesser.add_guess(3)
        self.assertEqual(NumberGuesser.guessed_list, [5, 8, 3])


if __name__ == '__main__':
    unittest.main()

