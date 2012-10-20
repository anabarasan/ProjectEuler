'''
Problem1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_of_multiples_of_3_or_5(limit):
	'''
	(int) -> int
	
	Returns the sum of multiples of 3 or 5 till the limit specified.
	
	>>> sum_of_multiples_of_3_or_5(10)
	23
	'''
	num = 0
	_sum = 0
	
	while num < limit:
		if (num % 3 == 0) or (num % 5 == 0):
			_sum += num
		num += 1
	
	return _sum
	
print sum_of_multiples_of_3_or_5(1000)
