# test_modulo.py
import unittest
from modulo import modulo


class TestModuloFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(25, 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(modulo(-10, 3), -1)
        self.assertEqual(modulo(10, -3), 1)
        self.assertEqual(modulo(-10, -3), -1)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_zero_dividend(self):
        self.assertEqual(modulo(0, 5), 0)
        self.assertEqual(modulo(0, -5), 0)


if __name__ == '__main__':
    unittest.main()
