import requests
from bs4 import BeautifulSoup
import pprint
import json

# Extract the title of each recipe and save it as a variable
BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)

soup = BeautifulSoup(page.text)
links = soup.find_all('a')
titles = []
for link in links:
    titles.append(link.text)
# pprint.pprint(titles)

# Extract the text body of each recipe and save it as a variable
pages = [link['href'] for link in links]
recipes = []
for p in pages:
    p1 = requests.get(f'https://codingnomads.github.io/recipes/{p}')
    recipe = BeautifulSoup(p1.text)
    info = recipe.find('div', class_='is-normal')
    # info = recipe.find('div', class_='md')
    recipes.append(info.text)
# print(info.text)
with open('recipe_data.json', 'w') as fout:
    json.dump(recipes, fout)


url = 'https://codingnomads.github.io/recipes/recipes/68-kimchi-fried-rice-wi.html'
new_page = requests.get(url)
more_soup = BeautifulSoup(new_page.text)
author = more_soup.find('p', class_='author')
# kimchi = more_soup.find_all('p', class_=False, id=False)
kimchi = more_soup.find('div', class_='md')


# pprint.pprint(author.text.strip('by'))
# pprint.pprint(kimchi.text)
