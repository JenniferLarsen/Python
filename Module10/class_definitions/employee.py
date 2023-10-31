from datetime import datetime

"""
Jennifer Larsen
10/30/2023
This program explores writing and using Classes and Tests
"""


class Employee:
    def __init__(self, last_name, first_name, address, phone_number, salaried, start_date, salary):
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._salary = salary
        self._start_date = start_date

    def display(self):
        employment_type = "Salaried" if self._salaried else "Hourly"
        rate = f"${self._salary}/year" if self._salaried else f"${self._salary:.2f}/hour"
        formatted_start_date = self._start_date.strftime("%m-%d-%Y")

        return f"{self._first_name} {self._last_name}\n{self._address}\nSalaried employee: {rate}\nStart date: {formatted_start_date}"

    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()


employee = Employee("Patel", "Sasha", "123 Main Street", "Urban, Iowa", True, datetime(2019, 6, 28), 40000)
employee2 = Employee("Last", "First", "321 Any Street", "City, Iowa", False, datetime(2020, 10, 30), 15.28)


print(str(employee))
print(repr(employee))


print(str(employee2))
print(repr(employee2))
