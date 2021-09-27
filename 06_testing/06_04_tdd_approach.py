# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest

class TestGeneralArithmetic(unittest.TestCase):
    def test_addition(self):
        a = 6
        b = 5
        self.assertEqual(addition(a, b), 11)
    def test_subtraction(self):
        a = 4
        b = -11
        self.assertEqual(subtraction(a, b), 15)
    def test_multiplication(self):
        a = 14
        b = 2
        self.assertEqual(multiplication(a, b), 28)
    def test_division(self):
        a = 15
        b = 3
        self.assertEqual(division(a, b), 5)