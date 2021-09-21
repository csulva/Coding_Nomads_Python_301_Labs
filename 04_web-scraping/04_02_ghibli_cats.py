# Read through the documentation of the Ghibli API and reproduce the example
# listed at https://ghibliapi.herokuapp.com/#section/Use-Case in Python.
# Try skim the Haskell code example and see if you can understand anything.
# Don't worry if you don't, it's a completely different language :)
#
# Your task is to use the API to find information about all the cats that
# appear in Studio Ghibli films.
from typing import NewType
import requests
# from bs4 import BeautifulSoup
import pprint
import json

BASE_URL = "https://ghibliapi.herokuapp.com/species"

request = requests.get(BASE_URL)
data = request.json()

list_of_cats = []
for x in data:
    if x['name'] == 'Cat':
        list_of_cats.append(x['people'])

cat_list = []
for cats in list_of_cats:
    for x in cats:
        new_url = f'{x}'
        new_request = requests.get(new_url)
        new_data = new_request.json()
        new_dict = {}
        for k, v in new_data.items():
            if k == 'name' or k == 'gender' or k == 'age' or k == 'eye_color' or k == 'hair_color':
                new_dict[k] = v
                cat_list.append(new_dict)
pprint.pprint(cat_list)