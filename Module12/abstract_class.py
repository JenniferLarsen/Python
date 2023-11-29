"""
Jennifer Larsen
11/24/2023
This program explores abstract classes.
"""

from abc import ABC, abstractmethod


class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


class Bicycle(Rider):
    def ride(self):
        return "Human powered, not enclosed"

    def riders(self):
        return "1 or 2 if tandem or a daredevil"


class Motorcycle(Rider):
    def ride(self):
        return "Engine powered, not enclosed"

    def riders(self):
        return "1 or 2"


class Car(Rider):
    def ride(self):
        return "Engine powered, enclosed"

    def riders(self):
        return "1 plus comfortably"


# Driver code
if __name__ == "__main__":
    bicycle = Bicycle()
    motorcycle = Motorcycle()
    car = Car()

    # Calling methods for each object
    print("Bicycle:")
    print(bicycle.ride())
    print(bicycle.riders())
    print()

    print("Motorcycle:")
    print(motorcycle.ride())
    print(motorcycle.riders())
    print()

    print("Car:")
    print(car.ride())
    print(car.riders())
