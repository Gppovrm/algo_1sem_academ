import unittest
from src.Lab2.t_3 import merge_sort

class TestInversionCount(unittest.TestCase):
    def test_example_case(self):
        A = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 17)

    def test_sorted_array(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 0)

    def test_reverse_sorted_array(self):
        A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 45)

    def test_single_element_array(self):
        A = [1]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 0)

    def test_no_inversions(self):
        A = [5, 6, 7, 8, 9]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 0)

    def test_all_identical_elements(self):
        A = [2, 2, 2, 2, 2]
        self.assertEqual(merge_sort(A, [0]*len(A), 0, len(A) - 1), 0)

if __name__ == "__main__":
    unittest.main()
