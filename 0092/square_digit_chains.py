#solution to Project Euler challenge 92
#
#coded by Ian Ruotsala

LIMIT = 10000000 #do operation for all natural numbers below 10 million
ends_in_89 = set([89])
ends_in_1 = set([1])

def find_next_number(n):
	#return the sum of the squares of n's digits
	to_return = 0
	while True:
		to_return += (n % 10) * (n % 10)
		if (n / 10 == 0):
			return to_return
		n /= 10

def find_ending(n):
	path_to_solution = list() #keep track of all the numbers we had to iterate through

	#while n in not in either set, keep iterating
	while ((n not in ends_in_89) and (n not in ends_in_1)):
		path_to_solution.append(n)
		n = find_next_number(n)

	if n in ends_in_1:
		ends_in_1.add(n)
		ends_in_1.update(path_to_solution)
	else:
		ends_in_89.add(n)
		ends_in_89.update(path_to_solution)

def main():
	for n in range(2, LIMIT):
		find_ending(n)

	print len(ends_in_89)

main()
