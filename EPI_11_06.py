# Compute the k largest elements in a max heap
# Without modifying the heap
from Heap import *


def return_k_largest(heap, k):
    # takes a max heap, and a integer k, returns k largest elements from the heap
    k = min(heap._size(), k)

    max_heap = Heap()
    max_heap.insert(HeapNodes(heap.top(), 1))
    result = []
    for i in range(k):
        top = max_heap.pop_top()
        result.append(top.data)
        ndx = top.origin
        child = ndx * 2
        if child <= heap._size():
            max_heap.insert(HeapNodes(heap.nth(child), child))
        if child + 1 <= heap._size():
            max_heap.insert(HeapNodes(heap.nth(child + 1), child + 1))
    return result


if __name__ == '__main__':
    aheap = Heap([3, -1, 2, 6, 4, 6, 8])
    print aheap
    print return_k_largest(aheap, aheap._size())
    print return_k_largest(aheap, 1)