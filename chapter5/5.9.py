"""
Write a program that takes an integer argument and returns all the primes 
between 1 and that integer.


"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"


def find_primes(number):
	""" Returns all primes by applying sieve of Eratosthenese
	"""
	primes = []
	is_prime = [False,False] + [True] * (number-1)

	for p in range(2,number):
		if is_prime[p]:
			primes.append(p)

		# Eliminating all multiples of primes
		for j in range(p * 2, number+1, p):
			is_prime[j] = False

	print(is_prime)
	return primes

	


if __name__ == '__main__':

	print(find_primes(10))
