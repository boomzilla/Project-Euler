#circular_primes.py
#solution to Project Euler 35

import array

LIMIT=1000000 #find all circular primes below 1 million
TRUE = 1
FALSE = 0 #need these for the array

def check_rot(prime, is_prime_array, circ_primes):
	digit_count = 1
	prime_copy = prime
	while (prime_copy / 10 != 0):
		digit_count += 1
		prime_copy = prime_copy / 10

	composite_found = False
	for n in range (1,digit_count):
		prime = rotate(prime, digit_count)
		#print str(prime) + " is composite?"
		#print is_prime_array[prime]
		if (is_prime_array[prime] == FALSE):
			composite_found = True
			#print "composite found: " + str(prime)
		
	if (not composite_found):
		for n in range(0,digit_count):
			prime = rotate(prime, digit_count)
			circ_primes.add(prime)	

def rotate(number, digit_count):
	ones = number / int(10**(digit_count-1))	
	number = number - ones * int(10**(digit_count-1))
	number = number * 10 + ones
	return number

def main():
	print "starting"
	sqrt_limit = int(LIMIT**0.5) 
	is_prime_list = [FALSE, FALSE]

	#initialize the rest of list to True
	for m in range(2, LIMIT):
		is_prime_list.append(TRUE)

	#transfer list to array for quicker sieve
	is_prime_array = array.array('b', is_prime_list)

	for m in range(2, sqrt_limit):
		if (is_prime_array[m] == TRUE):
			for n in range(m*m, LIMIT, m):
				is_prime_array[n] = FALSE

	circ_primes = set()
	#print is_prime_array
	print "sieve done"
	for n in range(2, LIMIT):
		if is_prime_array[n] == TRUE:
			check_rot(n, is_prime_array, circ_primes)

	print len(circ_primes)
	#print circ_primes
main()
