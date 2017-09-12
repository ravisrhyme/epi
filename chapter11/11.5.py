"""
Compute the real number square root

We use binary search technique here.

Time Complexity  : O(log(k/s)) k is number, s is tolerance
Space Complexity : O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"


import math

def find_real_sqrt(number):

	# left and right varies basing on number between 0,1 or > 1
	# for 0<= number <= 1, sqrt lies between them and it will be
	# greater than number. between 0,1 many functions of numbers
	# have a reverse properties :)
	left,right = (number,1.0) if number < 1.0 else (1.0,number)

	# math.isclose checks whether two floating point numbers are 
	#close(10^-9)/equal

	while not math.isclose(left,right):
		mid = (left + right) * 0.5

		mid_square = mid * mid 
		if mid_square > number:
			right = mid
		else:
			left = mid

	return left


if __name__ == '__main__':
	
	print(find_real_sqrt(10))
