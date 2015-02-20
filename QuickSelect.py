# coding=UTF-8

"""
Created on 2/16/15

@author: 'johnqiao'
"""
import random


class QuickSelect():
    def __init__(self, vs, k, is_small=False):
        """
        :param vs: Integer array.
        :param k: K-th largest or smallest integer.
        :param is_small: For smallest or largest K-th integer.
        :return:
        """
        self.vs = vs
        self.k = k
        self.is_small = is_small

    def sort(self):
        return self._helper(self.vs, 0, len(self.vs) - 1, self.k, self.is_small)

    def _helper(self, vs, low, high, k, is_small):
        if low < high:
            pivot_index = self._partition(vs, low, high)
            if k == pivot_index:
                return vs[k]
            elif k < pivot_index:
                if is_small:
                    # TODO(sqiao): implement quick select for smallest K-th.
                    return None
                else:
                    return self._helper(vs, low, pivot_index - 1, k, False)
            else:
                if is_small:
                    # TODO(sqiao): implement quick select for smallest K-th.
                    return None
                else:
                    return self._helper(vs, pivot_index + 1, high, k, False)
        return vs[low]

    def _partition(self, vs, low, high):
        pivot = vs[random.randint(low, high)]
        while low < high:
            print low, high, pivot, vs
            while low < high and vs[low] <= pivot:
                low += 1
            while low < high and vs[high] > pivot:
                high -= 1
            if vs[low] > vs[high]:
                vs[low], vs[high] = vs[high], vs[low]
        return low


if __name__ == '__main__':
    values = [2, 3, 4, 1, 5, 6, 0, 9]
    qs = QuickSelect(values, 3)
    print qs.sort()

