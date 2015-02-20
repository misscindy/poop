# Search for the first element greater than k


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


if __name__ == "__main__":
    test_cases = [
        ([0, 0, 0, 1, 2, 2, 2, 4, 5, 6], 6),


    ]

    for a, t in test_cases:
        print search_first_greater(a, t)