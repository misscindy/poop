#########################
# Question 1
# Binary Search - Returns the number of occurrences of a target number in a sorted array.
# Muye Wang
#########################
def target_occurrence(array, target):
    # USELESS
    # 
    # target_index = _binary_search(array, 0, len(array) - 1, target)
    # if target_index == -1:
    #     print "not found"
    #     return 0

    # When found target:
    # Method 1:
    # running from mid to find the size
    # will take O(n) worst case [1,1,1,1,1,1,1], target = 1
    # Method 2:
    # use specialized binary search to find the first and last occurrence
    # last_index - first_index + 1 is the result

    first = _search_for_ending(array, target, 0, len(array) - 1)
    last = _search_for_ending(array, target, first, len(array) - 1, last=True)

    return last - first + 1


def _search_for_ending(array, target, lo, high, last=False):
    # [0, 1, 2, 3, 4, 4, 4 , 5, 5, 5, 6] target = 4
    # look for first
    # always going to return a valid index

    if lo >= high:
        return lo if array[lo] == target else -1
    
    mid = (lo + high) >> 1
    
    if array[mid] < target:
        return _search_for_ending(array, target, mid + 1, high, last)

    if array[mid] > target:
        return _search_for_ending(array, target, lo, mid - 1, last)

    elif array[mid] == target:
        if not last and (mid == 0 or array[mid] != array[mid - 1]):
            # reaching the left end
            return mid
        elif last and (mid == len(array) - 1 or array[mid] != array[mid + 1]):
            return mid
        else:
            return _search_for_ending(array, target, lo, mid - 1, last) if not last else _search_for_ending(array, target, mid + 1, high, last)


#########################
# Question 2
# Binary Search - Search for the fist occurrence of k.
# 
#########################
def binary_search(array, k):
    lo, high = 0, len(array) - 1

    while lo <= high:
        mid = (lo + high) >> 1
        if array[mid] == k:
            if mid == 0 or array[mid - 1] != k:
                return mid
            else:
                high = mid - 1
        elif array[mid] > k:
            high = mid - 1
        else:
            lo = mid + 1

    return -1


if __name__ == "__main__":
    # For Question 1
    test_cases = [
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 3), 2),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 7), 1),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 9), 1),
        (([1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 2), 4),
        (([1, 1, 1, 1, 1, 1], 1), 6),
        (([1, 1, 1, 1, 1], 1), 5),
        (([1], 1), 1),
    ]
    for test_case, expected in test_cases:
        print target_occurrence(test_case[0], test_case[1]) == expected
    

