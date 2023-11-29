class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass


class Customer:
    def __init__(self, customer_id, last_name, first_name, phone_number):
        self.validate_customer_id(customer_id)
        self.validate_name(last_name)
        self.validate_name(first_name)
        self.validate_phone_number(phone_number)

        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def validate_customer_id(self, customer_id):
        if not (1000 <= customer_id <= 9999):
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
