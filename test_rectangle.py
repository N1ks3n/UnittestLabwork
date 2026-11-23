import unittest

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area(3, 5), 15)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_zero_width(self):
        self.assertEqual(area(0, 7), 0)

    def test_area_zero_height(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_fractional(self):
        self.assertAlmostEqual(area(2.5, 1.2), 3.0)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(3, 5), 16)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_zero_width(self):
        self.assertEqual(perimeter(0, 7), 14)

    def test_perimeter_zero_height(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_fractional(self):
        self.assertAlmostEqual(perimeter(2.5, 1.2), 7.4)
