import unittest

from multiples import get_sum


class TestMultiples(unittest.TestCase):
    def test_multiples_bellow_10(self):
        self.assertEqual(23, get_sum(10))

    def test_multiples_bellow_1000(self):
        self.assertEqual(233168, get_sum(1000))


if __name__ == '__main__':
    unittest.main()
