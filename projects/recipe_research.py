# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.
import webbrowser

#Create Ingredients Class with name and amount
class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def __str__(self):
        return f'{self.name}: {self.amount}'

    #Create instance method .get_info() that takes .name attribute of an Ingredient() and creates a Wikipedia URL
    def get_info(self):
        return webbrowser.open(f'https://en.wikipedia.org/wiki/{self.name}')

    def __add__(self, other):
        soup = self.name + ' & ' + other.name
        min_amount = min(self.amount, other.amount)
        return f'You can make {min_amount} servings of {soup} soup!'


onion = Ingredient('onion', 4)
carrot = Ingredient('carrot', 5)

print(onion + carrot)
onion.get_info()