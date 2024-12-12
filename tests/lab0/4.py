import unittest
from src.Lab1.t_4 import linear_search

class TestLinearSearch(unittest.TestCase):
    def test_search_multiple_occurrences(self):
        array = [10, 20, 10, 30, 10]
        target = 10
        expected = (3, [0, 2, 4])
        self.assertEqual(linear_search(array, target), expected)

    def test_search_single_occurrence(self):
        array = [10, 20, 30]
        target = 20
        expected = (1, [1])
        self.assertEqual(linear_search(array, target), expected)

    def test_search_not_found(self):
        array = [10, 20, 30]
        target = 40
        expected = -1
        self.assertEqual(linear_search(array, target), expected)


if __name__ == '__main__':
    unittest.main()
