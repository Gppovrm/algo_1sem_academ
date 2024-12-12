import unittest
from src.Lab1.t_1 import InsertionSort

class TestInsertionSort(unittest.TestCase):
    def test_sort_random_array(self):
        self.assertEqual(InsertionSort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

    def test_sort_sorted_array(self):
        self.assertEqual(InsertionSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sort_reverse_array(self):
        self.assertEqual(InsertionSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
