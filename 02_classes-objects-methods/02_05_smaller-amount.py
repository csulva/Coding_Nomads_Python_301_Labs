# Update the __add__() method of `Ingredient()` so that instead of
# instantiating the new Ingredient() object with an amount of 1,
# it'll take whichever amount of the passed ingredients is smaller
#
# Example:
# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)
# s = c + p
# print(s)
# >>> OUTPUT: carrotpea (4)

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        if other.name == 'flamingo':
            return None
        new_name = other.name + self.name
        new_amount = self.amount, other.amount
        return Ingredient(name=new_name, amount = min(new_amount))
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"
    
    def __sub__(self, other):
        print('I am subtract')


if __name__ == '__main__':
    c = Ingredient("carrot", 6)
    p = Ingredient("pea", 8)
    n = Ingredient('flamingo', 1)
    s = p + c
    print(c + n)