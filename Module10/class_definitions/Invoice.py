"""
Jennifer Larsen
10/30/2023
This program explores writing and using Classes and Tests
"""


class Invoice:
    def __init__(self, invoice_id, customer_id, address, last_name, first_name, phone_number, items_with_price=None):
        if any(arg is None for arg in [invoice_id, customer_id, address, last_name, first_name, phone_number]):
            raise ValueError("All required arguments must be provided.")

        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.address = address
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.items_with_price = items_with_price if items_with_price is not None else {}

    def __str__(self):
        return f"Invoice ID: {self.invoice_id}\nCustomer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\nAddress: {self.address}\nPhone: {self.phone_number}"

    def __repr__(self):
        return f"Invoice({self.invoice_id}, {self.customer_id}, '{self.address}', '{self.last_name}', '{self.first_name}', '{self.phone_number}', {self.items_with_price})"

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        total = sum(self.items_with_price.values())
        tax = total * 0.06

        for item, price in self.items_with_price.items():
            print(f"{item}.....${price:.2f}")

        print(f"Tax......... ${tax:.2f}")
        print(f"Total.......${total + tax:.2f}")


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
