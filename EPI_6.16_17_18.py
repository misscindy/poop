# Sample Offline Data
# A : an array with distinct elements 
# return a subset of k elements of A. All subsets should be equally likely. 
# Use a few calls to the randome number gen, use O(1) additional storage 

import random 
def sample_subset(array, k):
	if len(array) < k: return None

	for i in range(len(array) - 1, len(array) - k - 1, -1):
		swap_i = random.randint(0,i)
		array[swap_i], array[i] = array[i], array[swap_i]

# 6.17
def random_permuation(array):
	sample_subset(array, len(array))

#6.18 

# todo 




if __name__ == '__main__':
	array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	sample_subset(array, 1)
	print array
	random_permuation(array)
	print array
