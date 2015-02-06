'''
Compute x * y without multiply or add 

Write a function that multiplies two nonnegative integers. 
The only operators you are allowed to use are assingment and bitwise ops
>> << | & ~ ^
Loops, conditionals, and functions 

'''

def multiply(a, b):
	# if either a or b is 0, return 0
	if a <= 0 or b <= 0: return 0 
	# 1011 * 101 
	cur_sum = 0 
	while a:
		if(a & 1):
			cur_sum = add(cur_sum, b)
		a, b = a >> 1, b << 1 
	return cur_sum

def add(a, b):
	sum = carryin = 0
	k, temp_a, temp_b = 1, a, b


	#  k = 1000  
	#  temp_a = 10101
	#  temp_b = 11111 
	#  carryin = 11111
	while(temp_a or temp_b):
		digit_a, digit_b = a & k, b & k 
		carry = carryin & digit_b | carryin & digit_a | digit_b & digit_a
		sum |= (carryin ^ digit_a ^ digit_b)
		carryin, k, temp_a, temp_b = carry << 1, k << 1, temp_a >> 1, temp_b >> 1
	return sum | carryin 




	
	


if __name__ == '__main__':
	# test_cases for add 
	test_cases = [ 
					((1, 1), 2),
					((0, 1), 1),
					((4, 1), 5),

					]		

	test_cases_mul = [

					((1, 1), 1),
					((1, 2), 2),
					((7, 2), 14),
					((10, 15), 150),


				]	
		

	for args, exp in test_cases:
		print add(*args), " == ", exp

	for args, exp in test_cases_mul:
		print multiply(*args), " == ", exp






