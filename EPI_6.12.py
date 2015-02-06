
# enumerate all primes up to n 
# given positive integer >= 2 


# Brute force 
import math
def enum_prime_bf(n):
	#if n == 3: print 3,
	for i in xrange(2, n):
		prime = True
		for d in xrange(2, int(math.sqrt(i))+1):
			if i % d == 0:
				prime = False 
				break
		if prime: print i,
	print   


def enum_prime_bf(n):
	def check(i):
		for d in xrange(2, int(math.sqrt(i))+1):
			if i % d == 0:
				return False
		return True
	#if n == 3: print 3,
	print [i for i in xrange(2, n) if check(i)]



def enumerate_numbers(n):
	def perculate(i):
		counter = 3
		while i * counter < n:
			aux[(i * counter - 3) / 2] = True 
			counter += 2
		# print
		# for i, e in enumerate(aux):
		#  	print i, (2 * i) + 3, e, 
		# print  

	aux = [False for i in range(n/2 - 1)]
	print 2,
	for i in range(3, n, 2):
		if not aux[(i - 3) / 2]:
			print i,
		# print "perculate, ", i,
		perculate(i)


if __name__ == '__main__':
	test_cases = [ 
			(2, []),
			(3, [2]),
			(4, [2, 3]),
			(5, [2, 3]),
			(14, [2, 3, 5, 7, 11, 13])

	]	

	for args, exp in test_cases:
		enum_prime_bf(args)
	enum_prime_bf(100)
	enumerate_numbers(100)

