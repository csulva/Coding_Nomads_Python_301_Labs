# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed
    def add(self, max_speed):
        self.max_speed += 5
        return self.max_speed
    def __repr__(self):
        return f'The new {self.year} {self.model} model has a max speed of {self.max_speed} MPH.'

bmw_5 = Car('BMW 5 Series', 2022, 155)
lexus_is = Car('Lexus IS', 2021, 143)

bmw_5.add(bmw_5.max_speed)
bmw_5.add(bmw_5.max_speed)
print(bmw_5)

