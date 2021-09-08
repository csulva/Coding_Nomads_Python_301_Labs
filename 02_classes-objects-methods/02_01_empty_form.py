# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Ingredient:
    def __init__(self, name, amount, taste):
        self.name = name
        self.amount = amount
        self.taste = taste
    def expire(self):
        print(f'Whoops, your {self.name} went bad')
        self.name = 'expired ' + self.name
    def __str__(self):
        return f'{self.name}: {self.amount}'
    def __repr__(self):
        return f'Ingredient(name={self.name}, amount={self.amount})'

p = Ingredient('peas', 100, 'Salty')

print(repr(p))