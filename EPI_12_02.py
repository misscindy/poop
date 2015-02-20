# Search for the first element greater than k
# Version 1: Search
# Version 2: Search and record current result
# Version 3: Variant -->


def search_first_greater(array, k):
    lo, high = 0, len(array) - 1
    while lo <= high:
        mid = (lo + high) >> 1
        print lo, mid, high
        if array[mid] <= k:
            lo = mid + 1
        else:
            high = mid - 1
        print lo, mid, high
        print
    return lo if lo < len(array) else -1


def search_first_greater_2(array, k):
    # record the result
    lo, high, result = 0, len(array) - 1, -1
    while lo <= high:
        mid = (lo + high) >> 1
        if array[mid] > k:
            result, high = mid, mid - 1
        else:
            lo = mid + 1
    return result


if __name__ == "__main__":
    test_cases = [
        ([0, 0, 0, 1, 2, 2, 2, 4, 5, 6], 6),
        ([0, 0, 0, 0, 0, 0, 2], 1),



    ]

    for a, t in test_cases:
        print search_first_greater(a, t)
        print search_first_greater_2(a, t)
        print "======"