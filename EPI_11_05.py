# Design an algorithm for computing the running median of a sequence
# Output the median for every new element
from Heap import *


def ui():
    min_heap = Heap(is_max=False)
    max_heap = Heap()
    next = input()
    while next != "":
        min_heap.insert(next)
        if min_heap._size() > max_heap._size() + 1:
            max_heap.insert(min_heap.pop_top())
        # print min_heap, max_heap
        running_median = min_heap.top() if min_heap._size() > max_heap._size() else (float(
            min_heap.top()) + max_heap.top()) / 2
        print str(running_median)
        next = input()

if __name__ == '__main__':
    ui()









