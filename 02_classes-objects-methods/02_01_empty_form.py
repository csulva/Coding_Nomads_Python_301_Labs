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

class Patient:
    def __init__(self, name, age, reason, history):
        self.name = name
        self.age = age
        self.reason = reason
        self.history = history
    def __repr__(self):
        if self.history != None:
            return f'Patient {self.name}, {self.age} years old, is here for {self.reason}. Past medical history includes {self.history}.'
        else:
            return f'Patient {self.name}, {self.age} years old is here for {self.reason}.'


p1 = Patient('Chris', 28, 'headache', None)
p2 = Patient('Ruud', 45, 'shoulder injury', 'migraines')
p3 = Patient('Johnny', 43, 'labs', 'appendicitis, IBS, fainting, dizziness')
print(p3)

