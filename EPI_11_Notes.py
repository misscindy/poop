'''
###########Priority Queue#############
###########Heap Sort In Place#############
## Ops
# Insert -> O(logn)
# deleteMax -> O(logn)
# Heap construction : 	O(n)
# Heapsort O(nlogn)
# In place, garantee nlogn, not stable
# Not used for :
## the inner loop is longer than quicksort
## the references (do not take advantage of locality)
'''


class heapNodes:
    def __init__(self, data, origin):
        self.data = data
        self.origin = origin

    def __repr__(self):
        return "%s" % self.data

class PriorityQueue:
    def __init__(self, ls=None):
        if not ls:
            self.data = [None]
            self.size = 0
        else:
            self.size = len(ls)
            ls.insert(0, None)
            self.data = ls
            self.build_heap()


    def swim(self, k):
        # percolate up
        # O(logn)
        while (k > 1 and self.data[k / 2] < self.data[k]):
            self.data[k / 2], self.data[k] = self.data[k], self.data[k / 2]
            k /= 2


    def insert(self, value):
        # [None, 10, 5, 6] insert 11
        # Size = 3 + 1
        # swim self.data[self.size]
        # insert at the end
        # swim up
        # O(logn)
        self.data.append(value)
        self.size += 1
        self.swim(self.size)


    def sink(self, k):

        # exchange with the larger children until
        # reach the end or greater than both children
        while (2 * k <= self.size):

            # the children
            j = 2 * k

            if (j < self.size and self._less_than(j, j + 1)): j += 1
            # pick the larger child
            if (not self._less_than(k, j)): break
            # swap parent - child
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j

    def delete_max(self):
        if not self.size: return

        # swap last element with 1st and sink first
        max_val = self.data[1]
        self.data[1] = self.data.pop()
        self.size -= 1

        self.sink(1)
        return max_val

    def _less_than(self, left, right):
        return self.data[left] < self.data[right]

    def build_heap(self):

        for i in range(self.size / 2, 0, -1):
            self.sink(i)

    def heap_sort(self):
        while self.size > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            self.size -= 1

    def __repr__(self):
        return "%s" % self.data


if __name__ == '__main__':
    aPQ = PriorityQueue()
    for i in range(10):
        aPQ.insert(i)

    print aPQ
    aPQ.insert(11)
    print aPQ
    aPQ.delete_max()
    print aPQ
    bPQ = PriorityQueue([1, 2, 4, 10])
    print bPQ
    bPQ.heap_sort()
    print bPQ

