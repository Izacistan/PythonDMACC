from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def sides(self):
        pass

class Triangle(Shape):

    def __init__(self):
        self.num_sides = 3

    # overrides abstract method with implementation
    def sides(self):
        return self.num_sides

    def __str__(self):
        return str(self.sides())

# Driver code
t = Triangle()
print(str(t))