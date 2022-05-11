import unittest
import random


class TestSort(unittest.TestCase):
    @staticmethod
    def sort_list(lst):
        return sorted(lst)
    def test_sort_empty_list(self):
        self.assertEqual([], TestSort.sort_list([]))

    def test_sort(self):
        j = 10
        while j<=100000:
            randomlist = random.sample(range(10, 30), 5)
            self.assertEqual(sorted(randomlist), TestSort.sort_list(randomlist))
            j*=10
