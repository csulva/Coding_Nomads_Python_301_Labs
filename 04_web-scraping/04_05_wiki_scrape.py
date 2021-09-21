# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
import requests
from bs4 import BeautifulSoup
import json
import pprint

URL = "https://en.wikipedia.org/wiki/Web_scraping"
response = requests.get(URL)
data = BeautifulSoup(response.text)

content = data.find('div', id='bodyContent')
links = content.find_all('a', class_=None)
list_of_links = []
for link in links:
    if '#' not in link['href']:
        list_of_links.append(link)

new_link = list_of_links[21].text
new_url = new_link.replace(' ', '_')
new_url = f'https://en.wikipedia.org/wiki/{new_url}'

new_response = requests.get(new_url)
new_data = BeautifulSoup(new_response.text)
text = new_data.find('div', class_='vector-body')

# with open('wiki_content.txt', 'w') as fout:
#     json.dump(text.text, fout)