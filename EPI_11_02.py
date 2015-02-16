# Sort an increasing-decreasing array
# k-increasing array
# O(n) running time
# Aux heap for sort
from EPI_11_01 import *
UP, DOWN = True, False


def sort_k_up_down_array(array):

    ls_arrays = []
    Dir = UP
    prev = 0
    for i in range(len(array) + 1):
        if((i == len(array))
           or ((Dir == UP) and array[i - 1] > array[i])
            or((Dir == DOWN) and array[i - 1] < array[i])
        ):
            if Dir == UP:
                print array[prev:i]
                ls_arrays.append(array[prev:i])
            else:
                ls_arrays.append(array[i - 1: prev - 1:-1])
            Dir = not Dir
            prev = i
    return merge_sort(ls_arrays)


# merge k sorted array
if __name__ == '__main__':
    input = [1, 2, 3, 0, 4, 5, 6, 3, 1]
    output = sorted(input)

    print sort_k_up_down_array(input) == output

