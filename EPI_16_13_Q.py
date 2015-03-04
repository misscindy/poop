# Let A be an array of n numbers.
# The pair of indices (i, j) is said to be inverted if i < j and A[i] > A[j].
# 
# Problem 16.13:
# Design an efficient algorithm that takes an array A of n numbers and 
# returns the number of inverted pairs of indices.


def count_inverted_pairs(vs):
    def merge_sort_helper(left, right):
        if left >= right:
            return 0
        mid = (right + left) >> 1
        return merge_sort_helper(left, mid) + merge_sort_helper(mid + 1, right) + _merge(left, mid, right)

    def _merge(left, mid, right):
        count = 0
        aux, left_runner, right_runner = [], left, mid + 1
        while left_runner <= mid and right_runner <= right:
            if vs[left_runner] < vs[right_runner]:
                aux.append(vs[left_runner])
                left_runner += 1
            if vs[left_runner] >= vs[right_runner]:
                # count += mid + 1 - left_runner
                aux.append(vs[right_runner])
                right_runner += 1
        while left_runner <= mid:
            aux.append(vs[left_runner])
            left_runner += 1
        while right_runner <= right:
            aux.append(vs[right_runner])
            right_runner += 1

        if aux:
            vs[left:right + 1] = aux

        return count

    return merge_sort_helper(0, len(vs) - 1)


if __name__ == '__main__':
    test_cases = [
        ([1, 5, 3, 2, 7], 3),
        ([1, 5, 3, 7, 2], 4),
        ([1, 3, 2], 1),
        ([2, 1], 1),
        ([5, 4, 3, 2, 1], 10),
    ]
    for test_case, exp in test_cases:
        count_inverted_pairs(test_case) == exp
        print test_case


