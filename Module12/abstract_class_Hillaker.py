from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass

#   SUBCLASSES
class Bicycle(Rider):

    def __init__(self):
        self.power_enclosed = "Human powered, not enclosed"
        self.number_of_riders = "1 or 2 if tandem or a daredevil"

    # overrides abstract method with implementation
    def ride(self):
        return self.power_enclosed

    def riders(self):
        return self.number_of_riders

    def __str__(self):
        return str(self.ride() + ", " + self.riders() + ".")

class Motorcycle(Rider):

    def __init__(self):
        self.power_enclosed = "Engine powered, not enclosed"
        self.number_of_riders = "1 or 2"

    # overrides abstract method with implementation
    def ride(self):
        return self.power_enclosed

    def riders(self):
        return self.number_of_riders

    def __str__(self):
        return str(self.ride() + ", " + self.riders() + ".")

class Car(Rider):

    def __init__(self):
        self.power_enclosed = "Engine powered, enclosed"
        self.number_of_riders = "1 to 6, depending on vehicle size"

    # overrides abstract method with implementation
    def ride(self):
        return self.power_enclosed

    def riders(self):
        return self.number_of_riders

    def __str__(self):
        return str(self.ride() + ", " + self.riders() + ".")


# Driver code
b = Bicycle()
print(str(b))

m = Motorcycle()
print(str(m))

c = Car()
print(str(c))
