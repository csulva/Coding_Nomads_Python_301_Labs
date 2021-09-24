# Write a unittest test suite to test the rescrape module

import unittest
import rescrape as r

class TestRescrape(unittest.TestCase):
    pass

    # requests can establish a connection and receive a valid response
    def test_get_page_content(self):
        r.get_page_content(r.BASE_URL)

    # the response contains HTML code
    def test_get_html_content(self):
        r.get_html_content(r.BASE_URL)
    
    # the HTML can be successfully converted to a Beautiful Soup object
    def test_make_soup_function(self):
        r.make_soup(r.get_html_content(r.BASE_URL))
    
    # can identify all links from the index page
    def test_get_recipe_links(self):
        r.get_recipe_links(r.make_soup(r.get_html_content(r.BASE_URL)))
    
    # can identify the author of a recipe
    def test_get_author(self):
        url = 'https://codingnomads.github.io/recipes/recipes/2-steak-and-eggs-in-ca.html'
        self.assertEqual(r.get_author(r.make_soup(r.get_html_content(url))), 'irharrier2')

    # can get the main recipe text
    def test_get_recipe(self):
        url = 'https://codingnomads.github.io/recipes/recipes/2-steak-and-eggs-in-ca.html'
        self.assertEqual(r.get_recipe(r.make_soup(r.get_html_content(url)))[0:4], 'Here')



if __name__ == "__main__":
    unittest.main()


