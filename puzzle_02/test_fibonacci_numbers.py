import unittest

from fibonacci_numbers import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_number_below_4000000(self):
        self.assertEqual(4613732, fibonacci())


if __name__ == '__main__':
    unittest.main()
