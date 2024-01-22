import unittest

from main import filter_numbers

class TestNumberFilter(unittest.TestCase):
    def test_filter_even_numbers(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        even_numbers = filter_numbers(numbers, lambda number: number % 2 == 0)
        self.assertEqual(even_numbers, [0, 2, 4, 6, 8])

    def test_filter_odd_numbers(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        odd_numbers = filter_numbers(numbers, lambda number: number % 2 != 0)
        self.assertEqual(odd_numbers, [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()
