import unittest

from recursion.power import power


class TestPower(unittest.TestCase):
    def test_negative_power(self):

        self.assertEqual(power(5, -6), pow(5, -6))

    def test_power(self):
        self.assertEqual(power(2, 1), pow(2, 1))

    def test_both_negative(self):
        self.assertEqual(power(-5, -5), pow(-5, -5))

    def test_float_power(self):
        self.assertEqual(power(-5.0, 5.3), 'invalid input')

    def test_input_integer_or_float(self):
        self.assertEqual(power('u', 8), 'invalid input')


if __name__ == '__main__':
    unittest.main()