# Version 1: Search for the first occurrence of k
# Version 2: Search for the last occurrence of k


def binary_search(array, k, last=False):
    lo, high = 0, len(array) - 1

    while lo <= high:
        mid = (lo + high) >> 1
        if array[mid] == k:
            if not last:
                if mid == 0 or array[mid - 1] != k:
                    return mid
                else:
                    high = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != k:
                    return mid
                else:
                    lo = mid + 1
        elif array[mid] > k:
            high = mid - 1
        else:
            lo = mid + 1

    return -1

# def binary_search_r(array, k, lo, high, last=False):
#     if high < lo: return -1
#     mid = (lo + high) >> 1
#     if array[mid] == k:
#
#         if last:


def b_search(array, k, last=False):
    lo, high, result = 0, len(array) - 1, -1
    while lo <= high:
        mid = (lo + high) >> 1
        if array[mid] == k:
            result = mid
            if last:
                lo = mid + 1
            else:
                high = mid - 1
        elif array[mid] > k:
            high = mid - 1
        else:
            lo = mid + 1
    return result




if __name__ == "__main__":
    print binary_search([1, 2, 2, 2, 3, 3, 4, 5, 7], 2, True)
    print b_search([1, 2, 2, 2, 3, 3, 4, 5, 7], 2, True)