# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.imdb.com/title/tt0099864/trivia/?ref_=tt_trv_trv'
response = requests.get(url)
data = BeautifulSoup(response.text)

trivia = data.find('div', class_='article listo')
facts = trivia.find_all('div', class_='sodatext')

list_of_trivia = []
for x in facts:
    list_of_trivia.append(x.text)

# with open('it_facts.json', 'w') as fout:
#     json.dump(list_of_trivia, fout)

with open('it_facts.json', 'r') as fin:
    data = json.load(fin)

print(data[19])