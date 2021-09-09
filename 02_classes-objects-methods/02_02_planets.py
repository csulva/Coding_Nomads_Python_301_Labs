# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    
    def __init__(self, name, type, color, position, moons):
        self.name = name
        self.type = type
        self.color = color
        self.position = position
        self.moons = moons
    def __str__(self):
        return f'{self.name} is {self.type} & {self.color}, position # {self.position}, moons = {self.moons}'
    def __repr__(self):
        return f'{self.name} is a {self.type} and {self.color} planet, and is planet number {self.position} away from the sun. The number of moons it has: {self.moons}'

mercury = Planet('Mercury', 'rocky', 'grey', 1, None)
venus = Planet('Venus', 'rocky', 'yellow', 2, None)
earth = Planet('Earth', 'rocky', 'blue', 3, 1)
mars = Planet('Mars', 'rocky', 'red', 4, 2)

print(repr(earth))