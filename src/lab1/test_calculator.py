import unittest
from .calculator import to_number, sub, sum, div, multiply

class CalculatorTestCase(unittest.TestCase):
    def test_to_number(self):
        self.assertEqual(to_number("1"), 1)
        self.assertEqual(to_number("1.0"), 1)
        self.assertEqual(to_number("a"), "string")
    def test_sum(self):
        self.assertEqual(sum(2, 2), 4)
        self.assertEqual(sum(-2, 2), 0)
        self.assertEqual(sum(0, 1), 1)

    def test_sub(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(-2, 3), -5)
        self.assertEqual(sub(0, 1), -1)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(10, 0), "Деление на ноль")
        self.assertEqual(div(-10, 2), -5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-2, 8), -16)
        self.assertEqual(multiply(0, 1), 0)