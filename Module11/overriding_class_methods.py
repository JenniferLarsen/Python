"""
Jennifer Larsen
11/8/2023
This program creates employee and hourly and salaried employee classes that use overridden methods and displays data.
"""


from datetime import date


class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Name: {self.name}"


class SalariedEmployee(Employee):
    def __init__(self, name, start_date=date.today(), salary=40000):
        super().__init__(name)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, new_salary):
        self.salary = new_salary

    def display(self):
        return super().display() + f"\nStart Date: {self.start_date}\nSalary: ${self.salary:.2f}"

    def pay(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, name, start_date=date.today(), hourly_pay=10.00):
        super().__init__(name)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, new_hourly_pay):
        self.hourly_pay = new_hourly_pay

    def display(self):
        return super().display() + f"\nStart Date: {self.start_date}\nHourly Pay: ${self.hourly_pay:.2f}"

    def pay(self, hours_worked):
        return self.hourly_pay * hours_worked


# Driver for SalariedEmployee
salaried_employee = SalariedEmployee("John Doe")
print("Salaried Employee Information:")
print(salaried_employee.display())
salaried_employee.give_raise(45000)
print("\nUpdated Salaried Employee Information:")
print(salaried_employee.display())

# Driver for HourlyEmployee
hourly_employee = HourlyEmployee("Jane Smith")
print("\nHourly Employee Information:")
print(hourly_employee.display())
hourly_employee.give_raise(12.00)
print("\nUpdated Hourly Employee Information:")
print(hourly_employee.display())
