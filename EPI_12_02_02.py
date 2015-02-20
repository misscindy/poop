
# Muye Wang
# returns the number of occurrences of a target number in a sorted array.


# test_cases = [
# (([0, 1, 1, 1, 2, 2, 3], 1), 3),
#     (([0, 1, 1, 1, 2, 2, 3], 2), 2),
#
# ]
#
# result
# 3 == 3
# 2 == 2


def target_occurrence(array, target):
    target_index = _binary_search(array, 0, len(array) - 1, target)
    if target_index == -1:
        print "not found"
        return 0

    # When found target:
    # Method 1:
    # running from mid to find the size
    # will take O(n) worst case [1,1,1,1,1,1,1], target = 1
    # Method 2:
    # use specialized binary search to find the first and last occurrence
    # last_index - first_index + 1 is the result

    first = _search_for_ending(array, target, 0, target_index)
    last = _search_for_ending(array, target, target_index, len(array) - 1, last=True)
    return last - first + 1


def _search_for_ending(array, target, lo, high, last=False):
    # [0, 1, 2, 3, 4, 4, 4 , 5, 5, 5, 6] target = 4
    # look for first
    # always going to return a valid index
    mid = (lo + high) >> 1
    if array[mid] < target:
        # last == False
        return _search_for_ending(array, target, mid + 1, high)

    if array[mid] > target:
        # last == True
        return _search_for_ending(array, target, lo, mid - 1, True)

    elif array[mid] == target:
        if not last and (mid == 0 or array[mid] != array[mid - 1]):
            # reaching the left end
            return mid
        elif last and (mid == len(array) - 1 or array[mid] != array[mid + 1]):
            return mid

    else:
        return (_search_for_ending(array, target, lo, mid)
                if not last else _search_for_ending(array, target, mid, high))


# binary_search helper
def _binary_search(array, lo, high, target):
    # return target index if found, else -1
    if lo > high:
        return -1
    mid = (lo + high) >> 1
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return _binary_search(array, lo, mid - 1, target)
    else:
        return _binary_search(array, mid + 1, high, target)


# if __name__ == '__main__':
#
# test_cases = [
# (([0, 1, 1, 1, 2, 2, 3], 1), 3),
#         (([0, 1, 1, 1, 2, 2, 3], 2), 2),
#
#     ]
#
#     for arg, exp in test_cases:
#         print target_occurrence(*arg), "==", exp
#
#
