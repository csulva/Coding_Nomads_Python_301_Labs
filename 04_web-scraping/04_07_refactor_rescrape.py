# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

from os import read
import requests 
from bs4 import BeautifulSoup
import json

def scrape(url):
    response = requests.get(url)
    data = BeautifulSoup(response.text)
    return data

def search_scrape(data, div, cla):
    web_text = data.find_all(div, class_=cla)
    return web_text

def write_to(data, file_name):
    with open(f'{file_name}', 'w') as fout:
        json.dump(data, fout)

def read_in(file_name):
    with open(f'{file_name}', 'r') as fin:
        data = json.load(fin)
        return data


test = search_scrape(scrape('https://www.imdb.com/title/tt0099864/trivia/?ref_=tt_trv_trv'), 'div', None)
# write_to(str(test), 'test.txt')
data = read_in('test.txt')
print(data)