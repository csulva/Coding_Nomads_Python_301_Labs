# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest
import math

class TestMath(unittest.TestCase):
    def testSqrt(self):
        self.assertEqual(math.sqrt(36), 6)
    def testFloor(self):
        self.assertEqual(math.floor(5.4), 5)

if __name__ == "__main__":
    unittest.main()
