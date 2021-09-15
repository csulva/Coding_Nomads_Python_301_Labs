# create a custom Soup() class that can take Ingredient() and Spice() objects, 
# and use them to look up soup recipes on the Internet.
# Your Soup() objects should at least be able to:
    # take an unlimited number of Ingredient() or Spice() objects during instantiation
    # have a .cook() method that returns a search result for a soup recipe using all the added ingredients

from Ingredients_Class import Ingredient, Spice


# class Soup:
#     def __init__(self, name):
#         self.name = name
    
#     def cook(self, spice, ingredient):
#         soup = spice.name + ingredient.name
#         print(soup)

s = Spice('pepper', 300, 'spicy')
pickle = Ingredient('pickles', 14)

print(pickle)

