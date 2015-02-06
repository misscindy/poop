'''
# Check if a decimal integer is a Palindrome  

'''

def isPalindrome(x):
	if x == 10 or x < 0: return False 
	if x < 10: return True  
	temp, high = x//10, 1
	while temp: 	
		high *= 10
		temp //= 10

	lo = 10
	while lo < high: 
		print x, lo, high
		if (x % lo) != (x // high): return False 
		lo, high = lo * 10, high // 10 

	return True 



if __name__ == '__main__':
	test_cases = [
					((1), True),
					((10), False),
					((1001), True),
					((111111), True),
				]		


	for args, exp in test_cases:
		print isPalindrome(args), " == ", exp


