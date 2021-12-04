# For this project, your task is to create a CLI that takes as an input
# the names of ingredients from a user. Then, your code will fetch
# the recipe information from the CodingNomads recipe collection,
# and search through the text of the recipes to find ones that include
# the provided ingredients.
#
# Note: Feel free to integrate your custom Ingredient() and Soup() classes
# into the code base, to get some additional practice in working with your
# custom Python classes.

# Imports
import requests
from bs4 import BeautifulSoup
import json
import time

# URL = "https://codingnomads.github.io/recipes"
# response = requests.get(URL)
# data = response.text

# print(type(data))
with open ('04_web-scraping/recipe_data.json', 'r') as fin:
    data = json.load(fin)


# Create the search function
def search_recipes(recipes, ingredients):
    for recipe in recipes:
        if all(ingredient in recipe for ingredient in ingredients):
            print(recipe)

# Do the searching
list_of_ingredients = []
ingredient = input('What ingredient do you have? type "stop" to stop... ')
list_of_ingredients.append(ingredient)
while ingredient != 'stop'.lower():
    ingredient = input('What else? type "stop" to stop... ')
    if ingredient == 'stop'.lower():
        print('searching for recipes...')
        time.sleep(2)
        search_recipes(data, list_of_ingredients)
    list_of_ingredients.append(ingredient)




