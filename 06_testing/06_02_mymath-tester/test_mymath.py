# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `ZeroDivisionError` gets raised correctly.

import unittest
from mymath import subtract_divide

class TestSubtractThenDivide(unittest.TestCase):
    def test_subtract_then_divide(self):
        a = 2.5
        b = subtract_divide(10, 7, 3)
        self.assertEqual(b, a)
    def test_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            subtract_divide(10, 7, 7)


if __name__ == "__main__":
    unittest.main()
