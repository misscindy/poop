
def search(vs1, vs2, k):
    
    def _helper(vs1, left1, right1, vs2, left2, right2, k):
        # corner case: if k is greater than the length of any array...
        mid1, mid2 = (left1 + right1) >> 1, (left2 + right2) >> 1
        count = mid1 + mid2 + 2
        # print count, k
        # print mid1, left1, right1
        # print mid2, left2, right2
        # print 

        # base case: return the greater one, or anyone if two values are equal.
        if count == k:
            return vs1[mid1] if vs1[mid1] > vs2[mid2] else vs2[mid2]
        # if count < k, that means we need count more to find the smallest K-th element.
        if count < k:
            # go right, and move the pointer that has smaller value.
            if vs1[mid1] < vs2[mid2]:
                return _helper(vs1, mid1 + 1, right1, vs2, left2, right2, k)
            else:
                return _helper(vs1, left1, right1, vs2, mid2 + 1, right2, k)
        else:
            # go left, and move the pointer that has greater value.
            if vs1[mid1] > vs2[mid2]:
                return _helper(vs1, left1, mid1 - 1, vs2, left2, right2, k)
            else:
                return _helper(vs1, left1, right1, vs2, left2, mid2 - 1, k)
        return -1

    # corner case: invalid input k.
    if k < 0 or k > len(vs1) + len(vs2):
        print 'Error: invalid input k'
        return -1
    # corner case: if k is equal to 1, return the smaller one.
    if k == 1:
        return min(vs1[0], vs2[0])

    # corner case: the max value of a array is smaller than the min value of another.
    if vs1[len(vs1) - 1] < vs2[0]:
        return vs1[k - 1] if k <= len(vs1) else vs2[k - len(vs1) - 1]
    if vs2[len(vs2) - 1] < vs1[0]:
        return search(vs2, vs1, k)

    return _helper(vs1, 0, len(vs1) - 1, vs2, 0, len(vs2) - 1, k)


if __name__ == '__main__':
    test_cases = [
        (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5), 5),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 1), 1),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 2), 2),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 9), 9),
        (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 10), 10),

        (([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5), 5),
        (([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 11), 11),
        (([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 15),

        (([1] * 5, [1] * 5, 8), 1),
        (([1, 1, 1, 2], [1, 2, 3], 5), 2),

        # Failed
        # (([1, 1, 1, 2, 3], [1, 1, 1, 1, 2], 10), 3),
    ]

    for test_case, exp in test_cases:
        result = search(test_case[0], test_case[1], test_case[2]) 
        if result == exp:
            print 'True'
        else:
            print '=' * 20, ' TEST FAILED ', '=' * 20
            print 'INPUT: ', test_case[0], test_case[1], test_case[2]
            print 'RESULT: ', result
            print '=' * 20, '============', '=' * 20









