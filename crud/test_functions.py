import math
import unittest

from . import functions


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        """Test area"""
        self.assertAlmostEqual(functions.circle_area(1), math.pi)
        self.assertAlmostEqual(functions.circle_area(0), 0)
        self.assertAlmostEqual(functions.circle_area(2.1), math.pi * (2.1)**2)

    def test_values(self):
        self.assertRaises(ValueError, functions.circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, functions.circle_area, "radius")


if __name__ == "__main__":
    unittest.main()