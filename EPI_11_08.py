# Given an array, find k elements which are closest to the median
# [7, 14, 10, 12, 2, 11, 29, 3, 4] k = 5 -> [7, 14, 10, 12, 11]


def partition(array, lo, high):
    # return kth element
    # use last one as pivot
    i, j, pivot = lo, high - 1, high
    while i <= j:

        while i < high and array[i] <= array[pivot]:
            i += 1
        while j >= lo and array[j] > array[pivot]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
            # print i, j
            # print array, i, j

    # print pivot, j
    array[pivot], array[i] = array[i], array[pivot]
    return i


def quick_select(array, k):
    lo, high = 0, len(array) - 1
    if k > len(array) or k < 1:
        return "Error"
    while lo <= high:
        i = partition(array, lo, high)
        if i < k - 1:
            lo += 1
        elif i == k - 1:
            return array[i]
        else:
            high -= 1


# a = [3, 2, 4, 3, 2, 4, 5, 3]
# b = [2, 5, 7, 6, 4, 3, 2, 1, 4]
# c = [1, 2, 3, 4, 5, 4]
d = [5, 2, 3, 7, 6, 4, 2]
c = [quick_select(d, i) for i in range(1, len(d) + 1)]
print sorted(d) == c
print

#
# quick_select(a, 3)
# quick_select(b, 1)
# print "c"
# i = partition(d, 0, len(d) - 1)
# # print d, i
# i = partition(d, i + 1, len(d) - 1)
#
# print d, i
#
# print c
# print a
# print b









