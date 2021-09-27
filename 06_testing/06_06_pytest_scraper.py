# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import requests
from bs4 import BeautifulSoup

url = "https://codingnomads.github.io/recipes/"

def get_web_data(url):
    response = requests.get(url)
    return response

def get_html_from_webpage(url):
    html = get_web_data(url).text
    return html

def clean_up_html_with_beautiful_soup(html):
    data = BeautifulSoup(html, 'html.parser')
    return data

def get_titles_of_recipes_from_webpage_html(soup):
    titles = soup.find('div', class_='content is-normal')
    return titles.text

# def test_get_html_from_webpage():
#     assert "<!DOCTYPE hmtl>" in (get_html_from_webpage(url))


x = clean_up_html_with_beautiful_soup(get_html_from_webpage(url))
p = get_titles_of_recipes_from_webpage_html(x).strip()

def test_get_titles_of_recipes_from_webpage_html():
    assert p[0] == 'I'

def test_get_web_data():
    assert get_web_data(url).status_code == 200