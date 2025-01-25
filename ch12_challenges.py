import math

class Apple:
    def __init__(self, color, age, family, size):
        self.color = color
        self.age = age
        self.family = family
        self.size = size
        
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """ Calculates and returns a Circle's area."""
        return math.pi * (self.radius ** 2)

cir1 = Circle(2)
print(cir1.calculate_area())

class Triangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        """ Calculates and returns a Triangle's area."""
        return (self.width * self.length)/2

tri1 = Triangle(10, 5)
print(tri1.calculate_area())

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        """ Measurements of all six sides of the hexagon."""
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        """ Calculates and returns a Hexagon's perimeter."""
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hex1 = Hexagon(3,3,2,3,4,4)
print(hex1.calculate_perimeter())
