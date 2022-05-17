from src.quick_sort import Sort
from src.quick_sort import KthSmallest
from src.quick_sort import partition
from src.quick_sort import findMedian
import time
import numpy

def check_Sort():
    for count_of_elems in range(100, 10**5, 100):
        mas = list(numpy.random.randint(0, 10 ** 6, count_of_elems))
        start = time.time()
        Sort(mas)
        finish = time.time() - start
        with open('analytics_data/analytic_Sort.txt', 'a') as file:
            file.write(f'{count_of_elems} {finish}\n')

if __name__ == '__main__':
    check_Sort()
