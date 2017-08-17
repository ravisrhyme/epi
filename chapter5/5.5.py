"""
Delete duplicate elements from the sorted array.

Time Complexity = O(n)
Space Complexity = O(1)
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"


def remove_duplicates(elements_list):
	""" Clears Duplicate elemets from the list
	"""	
	sorted_index = 1
	for i in range(1,len(elements_list)):
		if elements_list[i] != elements_list[i-1]:
			elements_list[sorted_index] = elements_list[i]
			sorted_index += 1

	while sorted_index < len(elements_list):
		elements_list[sorted_index] = 0
		sorted_index += 1
		 


if __name__ == '__main__':

	elements_list = [2,3,5,5,7,11,11,11,13]
	print("Given List :", elements_list)
	remove_duplicates(elements_list)
	print("Processed List :",elements_list)

