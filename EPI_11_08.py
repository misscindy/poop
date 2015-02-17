# Given an array, find k elements which are closest to the median
# [7, 14, 10, 12, 2, 11, 29, 3, 4] k = 5 -> [7, 14, 10, 12, 11]


def quick_select(array, k):
    # return kth element
    # use last one as pivot
    i, j, pivot = 0, len(array) - 2, len(array) - 1
    counter = 1
    while i <= j:

        while i < len(array) and array[i] <= array[pivot]:
            i += 1
        while j >= 0 and array[j] > array[pivot]:
            j -= 1
        # print i, j, pivot, array
        print "%i iteration"%counter, i, j, array
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
            print i, j
            # print array, i, j
        counter += 1
    # print pivot, j
    array[pivot], array[i] = array[i], array[pivot]


# a = [3, 2, 4, 3, 2, 4, 5, 3]
# b = [2, 5, 7, 6, 4, 3, 2, 1, 4]
# c = [1, 2, 3, 4, 5, 4]
d = [5, 2, 3, 7, 6, 4, 2, 4]
#
# quick_select(a, 3)
# quick_select(b, 1)
# print "c"
quick_select(d, 1)
print d
#
# print c
# print a
# print b








