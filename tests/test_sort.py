import unittest
import random
from src.quick_sort import Sort


class TestSort(unittest.TestCase):

    def test_sort_empty_list(self):
        a = []
        Sort(a)
        self.assertEqual([], a)

    def test_sort(self):
        j = 10
        while j <= 100000:
            randomlist = random.sample(range(10, 30), 5)
            unsorted = randomlist.copy()
            Sort(randomlist)
            self.assertEqual(sorted(unsorted), randomlist)
            j *= 10
