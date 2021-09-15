# create a custom Soup() class that can take Ingredient() and Spice() objects, 
# and use them to look up soup recipes on the Internet.
# Your Soup() objects should at least be able to:
    # take an unlimited number of Ingredient() or Spice() objects during instantiation
    # have a .cook() method that returns a search result for a soup recipe using all the added ingredients

from Ingredients_Class import Ingredient, Spice
import webbrowser

class Soup:
    def __init__(self, name, *args):
        self.name = name
        self.args = args
    
    def cook(self):
        string = ''        
        for x in self.args:
            string += f'{x}+'
        string += 'soup+recipe'
        webbrowser.open(f'https://www.google.com/search?q={string}')

s = Spice('pepper', 300, 'spicy')
pickle = Ingredient('pickles', 14)
onion = Ingredient('onions', 14)
oregano = Spice('oregano', 400, 'earthy')

test = Soup('name', s.name, pickle.name, onion.name, oregano.name)

other_soup = Soup('Yummy', ['onions', 'chives', 'salt', 'cucumber'])
# other_soup.cook()
test.cook()