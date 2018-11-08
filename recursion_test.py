import unittest

from recursion.computelistsum import compute_sum


class Testcomputesum(unittest.TestCase):

    def test_computesum_with_negative_items(self):
        self.assertEqual(compute_sum([1, -2, -3, [4, 6]]), 6)

    def test_computesum(self):

        self.assertEqual(compute_sum([1, 2, 3, [4, 6]]), 16)

    def test_input_is_not_list(self):
        self.assertEqual(compute_sum((1, 2, 3)),
                         'Invalid argument type. This should be a list')


if __name__ == '__main__':
    unittest.main()