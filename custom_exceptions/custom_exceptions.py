"""
Jennifer Larsen
11/24/2023
This program explores custom exceptions and tests.
"""


from customer_exceptions import Customer, InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber):
        try:
            self.validate_customer_id(cid)
            self.validate_name(lname)
            self.validate_name(fname)
            self.validate_phone_number(pnumber)
        except (InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat) as e:
            raise e  # Re-raise the exception if validation fails

        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def validate_customer_id(self, customer_id):
        customer_id_characters = set("1234567890")
        if not customer_id_characters.issuperset(customer_id) or not (1000 <= int(customer_id) <= 9999):
            raise InvalidCustomerIdException("Invalid customer_id. Must be between 1000 and 9999.")

    def validate_name(self, name):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_characters.issuperset(name):
            raise InvalidNameException("Invalid name. Must contain only alphabetic characters.")

    def validate_phone_number(self, phone_number):
        phone_number_characters = set("1234567890-()")
        if not phone_number_characters.issuperset(phone_number) or not self.is_valid_phone_number_format(phone_number):
            raise InvalidPhoneNumberFormat("Invalid phone number format. Must be in the format 123-123-1234.")

    def is_valid_phone_number_format(self, phone_number):
        # You can implement your own validation logic for phone number format here
        # For simplicity, let's assume a basic check for the example
        return len(phone_number) == 12 and phone_number[3] == phone_number[7] == '-'

    def __str__(self):
        return f"{self.customer_id}: {self.last_name}, {self.first_name} Phone: {self.phone_number}"

# Driver code
# Valid customer


customer_one = Customer('123', 'Duck', 'Donald', '(555)555-5555')  # all required
print(str(customer_one))

# Invalid phone
# Wait! try/except needed!
try:
    customer_two = Customer('123', 'Duck', 'Donald', '(555)555-5555P')  # all required
except (ValueError, InvalidPhoneNumberFormat):
    print("Error found, customer not created")

# Invalid customer_id
# try/except needed
try:
    customer_three = Customer('ABC', 'Duck', 'Donald', '(555)555-5555')  # all required
except (ValueError, InvalidCustomerIdException):
    print("Error found, customer not created")

# Invalid first_name
# try/except needed!
try:
    customer_four = Customer('123', 'Duck', '2', '(555)555-5555')  # all required
except (ValueError, InvalidNameException):
    print("Error found, customer not created")
