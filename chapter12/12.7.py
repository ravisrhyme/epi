"""
Write a program which takes an array of strings and a set of srings,
and return the starting and ending index of a shortest subarray of the given 
array that "covers" the set i.e contains all strings in set.

Time Complexity  :
Space Complexity :
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"


import collections

def find_shortest_cover(paragraph,keywords):
	""" Returns the indices of shortest subarray that covers the
	given keywords.
	"""
	keywords_coverage = collections.Counter(keywords)
	remaining_words  = len(keywords)
	result = (-1,-1)
	left = 0

	for right, word in enumerate(paragraph):
		if word in keywords:
			keywords_coverage[word] -= 1
			if keywords_coverage[word] == 0:
				remaining_words -= 1

		# Once we get a subarray starting at left and ending at right with all
		# keywords covered, we do second pass over the subarray moving the left 
		# starting index to right side, i.e to get the smallest subarray.
		#  We break from loop once we move across atleast one word in keywords 
		while remaining_words == 0:

			if result == (-1,-1) or (right-left) < (result[1] - result[0]):
				result = (left,right)

			left_word = paragraph[left]
			
			# if the current start is one of keywords, we should break. Increment remaining_words
			if left_word in keywords:
				keywords_coverage[left_word] += 1
				if keywords_coverage[left_word] > 0:
					remaining_words += 1

			left += 1

	return result 
			
if __name__=='__main__':

	keywords = {'banana','cat'}
	paragraph = ['apple','banana','apple','apple','dog','cat','apple','dog','banana','apple','cat','dog']
	print(find_shortest_cover(paragraph,keywords))
