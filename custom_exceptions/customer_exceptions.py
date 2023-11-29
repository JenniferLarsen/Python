"""
Jennifer Larsen
11/24/2023
This program explores custom exceptions and tests.
"""

import re


class InvalidCustomerIdException(Exception):
    def __init__(self, message="Invalid customer_id. Must be between 1000 and 9999."):
        self.message = message
        super().__init__(self.message)


class InvalidNameException(Exception):
    def __init__(self, message="Invalid name. Must contain only alphabetic characters."):
        self.message = message
        super().__init__(self.message)


class InvalidPhoneNumberFormat(Exception):
    def __init__(self, message="Invalid phone number format. Must be in the format 123-123-1234."):
        self.message = message
        super().__init__(self.message)


class Customer:
    def __init__(self, cid, lname, fname, pnumber):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")

        if not customer_id_characters.issuperset(cid) or not (1000 <= int(cid) <= 9999):
            raise InvalidCustomerIdException("Invalid customer_id. Must be between 1000 and 9999.")

        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException("Invalid name. Must contain only alphabetic characters.")

        if not phone_number_characters.issuperset(pnumber) or not self.is_valid_phone_number_format(pnumber):
            raise InvalidPhoneNumberFormat("Invalid phone number format.")

        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def validate_customer_id(self, customer_id):
        if not (customer_id.isdigit() and 1000 <= int(customer_id) <= 9999):
            raise InvalidCustomerIdException("Invalid customer_id. Must be between 1000 and 9999.")

    def validate_name(self, name):
        if not name.isalpha():
            raise InvalidNameException("Invalid name. Must contain only alphabetic characters.")

    def validate_phone_number(self, phone_number):
        # This is a simple validation for demonstration purposes. In a real application, you may want to use a more
        # sophisticated validation, perhaps with regular expressions.
        if not (len(phone_number) == 12 and phone_number[3] == phone_number[7] == '-'
                and phone_number[:3].isdigit() and phone_number[4:7].isdigit() and phone_number[8:].isdigit()):
            raise InvalidPhoneNumberFormat("Invalid phone number format. Must be in the format 123-123-1234.")

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Last Name: {self.last_name}, " \
               f"First Name: {self.first_name}, Phone Number: {self.phone_number}"
