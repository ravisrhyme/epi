"""
Compute the integer square root

We use binary search technique here.

Time Complexity  : O(log(k)), k is given number
Space Complexity : O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"

def find_integer_sqrt(number):
	""" Finds nearest integer sqrt of a number by using 
	binary search.
	"""

	left, right = 0, number

	while left <= right:

		mid = (left + right) // 2
		mid_square = mid * mid 

		# Takes care of equality as well.
		# So we return left-1 at end and not left.
		# Important implementation technique to note!!
		if mid_square <= number:
			left = mid + 1
		else:
			right = mid - 1

	return left-1 


if __name__ == '__main__':
	
	print(find_integer_sqrt(21))
