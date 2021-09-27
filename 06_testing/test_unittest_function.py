import unittest_function06_03_ as u
import unittest

class test_unittest_function06_03_(unittest.TestCase):
    # Passes
    def test_area_of_circle_for_value(self):
        radius = 6
        self.assertEqual(u.area_of_circle(radius), 355.3057584392169)
    # Passes
    def test_area_of_circle_greater(self):
        radius = 6
        self.assertGreater(u.area_of_circle(radius), 100)
    # Fails
    def test_area_of_circle_strings(self):
        radius = 'six'
        self.assertEqual(u.area_of_circle(radius), 355.3057584392169)