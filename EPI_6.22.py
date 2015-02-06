# print n*n matrix in spiral order

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def print_spiral_matrix(matrix, res):
	'''
	 [	[1, 2, 3], 
	 	[4, 5, 6],
	 	[7, 8, 9] 
		]

	'''	
	n = len(matrix)
	start = 0 

	for level in range(n, 0, -2):

		# print top 
		res.extend(matrix[start][start:start + level])
		# print "t"
		# print matrix[start][start:start + level]
		
		# print right 
	
		for row in range(start + 1, start + level):
			res.append(matrix[row][start + level - 1])
		# 	print matrix[row][start + level - 1],

		# print 
		# print bottom 
		# print "t"
		res.extend(reversed(matrix[start + level - 1][start : start + level - 1]))
		# print list(reversed(matrix[start + level - 1][start : start + level - 1]))
		# print left 
		for row in range(start + level - 2, start, -1):
			res.append(matrix[row][start])
			# print matrix[row][start], 
			# print 

		start += 1 


test_cases =  [
				[ 	[1, 2, 3], 
		 			[4, 5, 6],
		 			[7, 8, 9] 
				], 
				[	[1,  2,  3,   4,  5,  6], 
				 	[7,  8,  9,  10, 11, 12],
				 	[13, 14, 15, 16, 17, 18],
				 	[19, 20, 21, 22, 23, 24],
				 	[25, 26, 27, 28, 29, 30],
				 	[31, 32, 33, 34, 35, 36]
				],
				[[2]]
			]



if __name__ == '__main__':
	res0, res1, res2 = [], [], []

	print_spiral_matrix(test_cases[0], res0)
	print res0
	print_spiral_matrix(test_cases[1], res1)
	print res1 
	print_spiral_matrix(test_cases[2], res2)
	print res2

	







