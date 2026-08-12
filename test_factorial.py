import unittest

from factorial import factorial


class FactorialTests(unittest.TestCase):
    def test_zero_and_one(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_positive_integer(self):
        self.assertEqual(factorial(5), 120)

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            factorial(2.5)


if __name__ == "__main__":
    unittest.main()
