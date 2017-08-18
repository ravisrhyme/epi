"""
Compute all Mnemonics for a phone number

Time Complexity  : O(4^n * n)
Space Complexity : O(4 ^ n)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"

mapping = ['0','1','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

def find_mnemonics(phone_number):
	""" Returns all mnemonics for a given phone number
	"""
	def helper(index):
		if index == len(phone_number):
			mnemonics.append(''.join(temp_list))
		else:
			for character in mapping[int(phone_number[index])]:
				temp_list[index] = character
				helper(index + 1)

	mnemonics = []
	temp_list = [0] * len(phone_number)
	helper(0)
	return mnemonics

if __name__=='__main__':
	phone_number = '242274'
	print(find_mnemonics(phone_number))
