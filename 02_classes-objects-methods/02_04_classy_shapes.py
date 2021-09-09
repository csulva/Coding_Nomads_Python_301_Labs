# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self, length, width):
        return length * width
    def perimeter(self, length, width):
        return (length * 2) + (width *2)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self, radius):
        return (math.pi * radius) ** 2
    def circumference(self, radius):
        return radius * 2 * math.pi

rectangle = Rectangle(4, 5)
circle = Circle(10)

print(circle.circumference(circle.radius))