# Permute the elements of an array 
# Given an array A of n Elements and a permutation P
# <2, 0, 1, 3> (a, b, c, d) -> (b, c, a, d)
# apply P to a, using constant additional storage


def apply_permutation(P, a):
	for index in range(len(P)):
		while index != P[index]:
			a[index], a[P[index]] = a[P[index]], a[index]
			element = P[index]
			P[index], P[element] = P[element], P[index]



if __name__ == '__main__':
	test_cases = [
				(([2, 0, 4, 1, 3, 5], ['a', 'b', 'c', 'd', 'e', 'f']), "bcad"),

	]		
	for (P , a), exp in test_cases:
		apply_permutation(P, a)
		print P, a


