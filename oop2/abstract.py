from abc import ABC, abstractmethod
from math import pi, pow

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Figure):

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return pi*pow(self.radius,2)

c = Circle(50)
print(c.area())