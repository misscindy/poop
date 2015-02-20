# Search for the fist occurrence of k


def binary_search(array, k):
    lo, high = 0, len(array) - 1

    while lo <= high:
        mid = (lo + high) >> 1
        print mid, lo, high
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
    print binary_search([1, 2, 2, 2, 3, 3, 4, 5, 7], 10000)



