"""
Jennifer Larsen
11/24/2023
This program explores custom exceptions and tests.
"""

import unittest
from customer_exceptions import Customer, InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class TestCustomerExceptions(unittest.TestCase):

    def test_valid_customer(self):
        customer = Customer('123', 'Duck', 'Donald', '(555)555-5555')
        self.assertEqual(str(customer), '123: Duck, Donald Phone: (555)555-5555')

    def test_invalid_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            Customer('123', 'Duck', 'Donald', '(555)555-5555P')

    def test_invalid_customer_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            Customer('ABC', 'Duck', 'Donald', '(555)555-5555')

    def test_invalid_first_name(self):
        with self.assertRaises(InvalidNameException):
            Customer('123', 'Duck', '2', '(555)555-5555')


if __name__ == '__main__':
    unittest.main()
