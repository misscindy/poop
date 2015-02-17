# Sort an almost sorted array
# A server may receives timestamped stock quotes
# and earlier quotes may arrive slightly after quotes because of differences in server loads and network routes
# TODO(bfan): check answer key
from Heap import *


def sort_sorted_array(array, k):
    # all elements are at most k aways from its correct position
    # O(nlogk) running time
    # O(k) extra space
    min_heap = Heap(is_max=False)
    # used to hold the k + 1 elements
    result = []
    ptr = 0

    while ptr < min(len(array), k + 1):
        min_heap.insert(array[ptr])
        ptr += 1

    while not min_heap.is_empty():
        result.append(min_heap.pop_top())
        if ptr < len(array):
            min_heap.insert(array[ptr])
            ptr += 1
    return result


if __name__ == '__main__':

    test_cases = [
        ([3, -1, 2, 6, 4, 5, 8]),

    ]
    for case in test_cases:
        print sort_sorted_array(case, 2)



