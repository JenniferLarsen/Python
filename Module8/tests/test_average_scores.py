"""
Jennifer Larsen
10/17/2023
This program is a unit test to test the average_scores.py program.
"""

import unittest
from more_fun_with_collections.average_scores import average_scores
# from directory.filename import function NOTE: yours might be named something else


class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
        self.scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual, 3)

    def test_average_five(self):
        # Arrange
        self.scores_dict = {"Test 1": 90, "Test 2": 89, "Test 3": 70, "Test 4": 98, "Test 5": 80}
        expected = 85.4
        # Act
        actual = average_scores(self.scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual, 3)

    def test_average_zero(self):
        # Arrange
        self.scores_dict = {}
        # Act
        # Assert
        with self.assertRaises(ValueError):
            actual = average_scores(self.scores_dict)
