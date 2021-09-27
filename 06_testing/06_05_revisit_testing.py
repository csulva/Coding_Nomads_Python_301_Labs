# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.

import requests
import unittest

url = 'http://demo.codingnomads.co:8080/tasks_api/users'
response = requests.get(url)
# print(response.json()['data'][0]['email'])

class TestApiEmailGets(unittest.TestCase):
    def test_get_list_of_emails(self):
        list_of_emails = []
        response = requests.get(url)
        email = response.json()
        for key, value in email.items():
            if key == 'data':
                new_value = value
                for dict in new_value[0::]:
                    for key, value in dict.items():
                        if key == 'email':
                            list_of_emails.append(value)
        self.assertEqual(list_of_emails[0], 'ozererva@outlook.com')

    def test_get_list_of_emails_with_less_code(self):
        a = response.json()['data']
        b = [dictionary for dictionary in a]
        c = b[0]['email']
        self.assertEqual(c, 'ozererva@outlook.com')

if __name__ == "__main__":
    unittest.main()