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
        print(f"whoops, the {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."

class Spice(Ingredient):

    def grind(self):
        print(f'You now have {self.amount} of ground {self.name}')
    
    def __add__(self, other):
        print(f'You now have a blend of {self.name} and {other.name}')
        print((self.name + ' & ' + other.name, min(self.amount, other.amount)))

p = Ingredient('Peas', 6)
print(p)
s = Spice('Salt', 200)
p = Spice('Pepper', 100)

s + p 
