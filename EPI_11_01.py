# Merge sorted files
# Individual files are sorted in increasing order of time
# TODO: (BFan) Implement heap with tuples <overload comparison operator>
# Idea: Use Aux heap and an aux array
from Heap import *


def merge_sort(ls_arrays):
    # heap to store the next first items from lists
    min_heap = Heap(is_max=False)

    # parallel array keep track of the next item
    next_items = [0] * len(ls_arrays)

    # push firsts on to heap
    for ndx, ele in enumerate(ls_arrays):
        if ele:
            next_items[ndx] += 1
            min_heap.insert(HeapNodes(ele[0], ndx))

    res = []
    while not min_heap.is_empty():
        # pop the next one from the heap --> O(logn)
        nxt = min_heap.pop_top()
        res.append(nxt.data)
        pos = nxt.origin
        # if still more to push on to the heap, push the next one and move pointer forward
        if next_items[pos] < len(ls_arrays[pos]):
            next_to_insert = ls_arrays[pos][next_items[pos]]
            min_heap.insert(HeapNodes(next_to_insert, pos))
            next_items[pos] += 1

    return res


if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5]], [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6]),


    ]
    for case, exp in test_cases:
        print merge_sort(case) == exp

'''
for files


'''


def open_multiple_files(ls_of_names):

    try:
        f = [open(file) for file in ls_of_names]

    finally:
        for fh in f:
            fh.close()