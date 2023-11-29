"""
Jennifer Larsen
11/8/2023
This program demonstrates multiple inheritance
"""

from datetime import date


class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Name: {self.name}"


class Employee:
    def __init__(self, name, start_date=date.today(), salary=40000):
        self.name = name
        self.start_date = start_date
        self.salary = salary

    def display(self):
        return f"Name: {self.name}\nStart Date: {self.start_date}\nSalary: ${self.salary:.2f}"


class Manager(Person, Employee):
    def __init__(self, name, department):
        Person.__init__(self, name)
        Employee.__init__(self, name, start_date=date.today())  # Set start_date to today
        self.department = department
        self.direct_reports = []

    def add_direct_report(self, employee):
        self.direct_reports.append(employee)

    def display_direct_reports(self):
        report_info = "\nDirect Reports:\n"
        for employee in self.direct_reports:
            report_info += employee.display() + "\n"
        return report_info

    def display(self):
        person_info = f"{Person.display(self)}\nStart Date: {self.start_date}\nDepartment: {self.department}"
        if self.salary is not None:
            person_info += f"\nSalary: ${self.salary:.2f}"
        return person_info


# Driver for Manager
manager = Manager("Jennifer Larsen", "Engineering")
print("Manager Information:")
print(manager.display())

# Create direct reports
employee1 = Employee("Employee One", date(2023, 1, 1), 45000)
employee2 = Employee("Employee Two", date(2023, 2, 1), 46000)
employee3 = Employee("Employee Three", date(2023, 3, 1), 47000)

# Add direct reports to the Manager
manager.add_direct_report(employee1)
manager.add_direct_report(employee2)
manager.add_direct_report(employee3)

# Display Manager and direct reports
print("Manager Information with Direct Reports:")
print(manager.display())
print(manager.display_direct_reports())

# Change salary
manager.salary = 42000
print("Updated Manager Information:")
print(manager.display())
