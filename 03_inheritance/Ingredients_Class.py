# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"Whoops, the {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."

class Spice(Ingredient):

    def __init__(self, name, amount, taste):
        super().__init__(name, amount)
        self.taste = taste

    def grind(self):
        print(f'You now have {self.amount} of ground {self.name}')
    
    def __add__(self, other):
        print(f'You now have a blend of {self.name} and {other.name}')
        print((self.name + ' & ' + other.name, min(self.amount, other.amount)))
    
    def expire(self):
        if self.name == 'salt' or self.name == 'salt'.capitalize():
            print(f'{self.name} never expires! You\'re good!')
        else:
            print(f"Your {self.name} has expired. it's probably still good.")
            self.name = 'old ' + self.name

class Vegetable(Ingredient):
    def __init__(self, name, amount, color):
        super().__init__(name, amount)
        self.color = color
    
    def chop(self):
        self.amount = self.amount * 5
        self.name = 'pieces of ' + self.name
    

p = Ingredient('Peas', 6)
print(p)
s = Spice('Salt', 200, 'salty')
pep = Spice('Pepper', 100, 'spicy')
salt = Ingredient('Salt', 100)

carrot = Vegetable('carrots', 5, 'orange')

carrot.chop()
print(carrot)
print(s.__hash__())


