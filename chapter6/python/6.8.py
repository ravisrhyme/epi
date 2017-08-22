"""
The Look-and-say Problem.

Look-and-say Sequence : 1,11,12,1112,3112..

Time Complexity  : O(n * k) k is the length of (n-1)th digit in sequence
Space Complexity : O(k)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"


def find_nth_number(n):
	""" Returns the nth number in look-and-say sequence
	"""
	temp = 1
	current_number = '1'
	temp_list = [] #List to hold all digits in next number

	while temp < n: # Takes care of sequence boundary
		del temp_list[:]
		current_index = 0
		# Traverses the current_number
		while current_index < len(current_number):

			repetitions, next_index = find_repetitions(current_number,current_index)
			temp_list.append(str(repetitions))
			temp_list.append(current_number[current_index])
			next_number = ''.join(temp_list)
			current_index  = next_index

		temp += 1
		current_number = next_number

	return current_number

def find_repetitions(current_number,i):
	""" Returns the number of repetitions of same digit starting from index i i.e count 
	and next index with new digit i.e j
	"""
	count = 1
	j = i + 1
	while j < len(current_number):
		if current_number[j] == current_number[i]:
			count += 1
			j += 1
		else:
			break
	
	return count, j



if __name__ == '__main__':
	print(find_nth_number(6))

