import unittest

from classes.calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_max_width_ramp(self):
        test_cases = [
            ([6, 0, 8, 2, 1, 5], 4),
            ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
            ([9, 8, 2, 0, 1, 9, 4, 0, 4, 1], 6),
            ([9, 8, 2, 1, 0, 9, 4, 0, 4, 1], 6),
            ([9, 8, 2, 1, 0, 9, 4, 0, 4, 2], 7),
            ([9, 8, 2, 1, 0, 9, 4, 0, 4, 8], 8),
            ([9, 8, 2, 1, 0, 9, 4, 0, 4, 9], 9),
            ([4, 0, 8, 2, 6, 7], 5),
            ([5, 4, 3], 0),
            ([2, 2, 1], 1)
        ]
        for input, expected in test_cases:
            # arrange & act
            result = self.calculator.max_width_ramp(input)

            # assert
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
