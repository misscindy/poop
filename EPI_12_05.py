# Search a sorted array of unknown length
# TODO(bfan): Other Methods


def search_k(array, k):
    exp = 0
    while True:
        try:
            val = array[(1 << exp) - 1]
            if val == k:
                return (1 << exp) - 1
            elif val > k:
                break
        except:
            break
        exp += 1

    left = max(0, 1 << (exp - 1))
    right = (1 << exp) - 2

    while left <= right:
        mid = (left + right) >> 1
        try:
            if array[mid] == k:
                return mid
            elif array[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        except:
            right = mid - 1
    return -1

#
# def locate(array, x):
#
#     try:
#         array[x]
#     except:
#         return None
#     return x
#
# def search_for_k(array, k):
#     exp = 0
#     while True:
#         if array[1 << exp - 1] and not array[1 << exp]:
#             return (1 << exp) - 1
#         elif not array[1 << exp - 1]:
#             exp += 1
#         else:
#
#




if __name__ == "__main__":
    # For Question 1
    test_cases = [
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 3), (5, 6)),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 7), 9),
        (([-1, 2, 2, 2, 2, 3, 3, 5, 5, 7, 9], 9), 10),
        (([1, 1, 1, 1, 5], 5), 4),
        (([1], 1), 0),
    ]
    for test_case, expected in test_cases:
        print search_k(test_case[0], test_case[1]), " == ", expected
