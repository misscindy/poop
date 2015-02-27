# Search in two sorted arrays
# Given an integer in [1, m+n]
# Variantion: find the


# brute force
def search(vs1, vs2, k):
    i, j, counter = 0, 0, 0
    while counter < k:
        if vs1[i] < vs2[j] or j == len(vs2):
            i += 1
        else:
            j += 1

        counter += 1
    print i, j, counter

    return max(vs1[i - 1] if i > 0 else None, vs2[j - 1] if j > 0 else None)

# log(k)
#
# def search_2(vs1, vs2, k):
#
#     a_end = min(len(vs1), k)
#     b_end = max(0, k - a_end)
#
#
#     print a_end, b_end




if __name__ == '__main__':
    test_cases = [
        (([1, 3, 5, 7, 9], [2, 3, 4, 6, 8, 10], 7), 4),
        (([1, 1, 1, 1, 1], [1, 2, 4, 4, 4, 10], 5), 1),
        (([0, 1], [0, 0], 1), 0),
        ]

    for test_case, exp in test_cases:
        # print search(test_case[0], test_case[1], test_case[2]) == exp
        print search(test_case[0], test_case[1], test_case[2])

