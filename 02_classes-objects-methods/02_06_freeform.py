# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Animal:
    def __init__(self, name, integument, speech, consumption, blood):
        self.name = name
        self.integument = integument
        self.speech = speech
        self.consumption = consumption
        self.blood = blood
        
    def __str__(self):
        return f'The {self.name} has {self.integument}, goes {self.speech}, eats {self.consumption}, and is {self.blood} blooded.'

    def __add__(self, other):
        return f'The {self.name} and {other.name} together have {self.legs + other.legs} legs.'

class Dog(Animal):
    def __init__(self, name, integument, speech, consumption, blood, breed, legs):
        super().__init__(name, integument, speech, consumption, blood)
        self.breed = breed
        self.legs = legs
    
    def __str__(self):
        return f'The {self.breed} breed of {self.name} has {self.integument}, goes {self.speech}, eats {self.consumption}, is {self.blood} blooded, and has {self.legs} legs.'

    def __add__(self, other):
        return ('total legs: ' + f'{(self.legs + other.legs)}')
    
class Bird(Animal):
    def __init__(self, name, integument, speech, consumption, blood, type, native):
        super().__init__(name, integument, speech, consumption, blood)
        self.type = type
        self.native = native
    def __str__(self):
        return f'The {self.type} type of {self.name} has {self.integument}, goes {self.speech}, eats {self.consumption}, is {self.blood} blooded, and native to {self.native}.'

class Snake(Animal):
    def __init__(self, name, integument, speech, consumption, blood, type, legs):
        super().__init__(name, integument, speech, consumption, blood)
        self.type = type
        self.legs = legs
    def __str__(self):
        return f'The {self.type} type of {self.name} has {self.integument}, goes {self.speech}, eats {self.consumption}, is {self.blood} blooded, and has {self.legs} legs.'
    def __add__(self, other):
        return super().__add__(other)

dog = Animal('dog', 'fur', 'bark', 'meat, plants', 'warm')
golden = Dog('dog', 'fur', 'ruff', 'meat, plants', 'warm', 'Golden Retriever', 4)
beagle = Dog('dog', 'fur', 'bark', 'plants', 'warm', 'Beagle', 4)
toucan = Bird('bird', 'feathers', 'croak', 'bugs, plants', 'warm', 'toucan', 'South America')
kiwi = Bird('bird', 'feathers', 'chirp', 'bugs, plants', 'warm', 'kiwi', 'Australia')
viper = Snake('snake', 'scales', 'hiss', 'birds, rodents, reptiles', 'cold', 'viper', 0)
python = Snake('snake', 'scales', 'hiss', 'birds, rodents, reptiles', 'cold', 'python', 0)

print(golden + python)