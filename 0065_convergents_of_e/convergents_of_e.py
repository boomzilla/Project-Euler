#my solution to Project Euler challenge 65
#http://projecteuler.net/problem=65
#
#number e can be expressed as infinite continued fraction (http://en.wikipedia.org/wiki/Continued_fraction):
#e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
#so, for 1st convergent, e ~= 2
#2nd convergent, e ~= 3
#3rd convergent, e ~= 8/3
#4th convergent, e ~= 11/4
#and so on
#
#find the numerator of 100th convergent, and sum up those digits
#
#Ian Ruotsala, 2013, June, 3rd

N_CONV = 100 #use 100th convergent

def find_gcd(a, b):
	while (b != 0):
		t = b
		b = a % t
		a = t
	return a

def find_numerator():
	numerator = 2
	denominator = 1

	for n in range(1, N_CONV+1):
		#add 1/denom_to_add to the fraction,
		#where denom_to_add progresses as 1,2,1,1,4,1, ..., 1,2k,1
		denom_to_add = 1
		if ((n+1) % 3 == 0):
			denom_to_add = (n+1)*2/3
		result = sum_fractions(numerator, denominator, 1, denom_to_add)
		#now simplify fraction		
		gcd = find_gcd(result[0], result[1])
		numerator = result[0]/gcd
		denominator = result[1]/gcd
	return numerator

def get_sum_of_digits(number):
	result = number % 10
	while (number / 10 != 0):
		result /= 10
		result += number % 10
	return result

def sum_fractions(numer_l, denom_l, numer_r, denom_r):
	#sum two fractions, return resultant numerator and denominator as a list of two items
	return [numer_l * denom_r + numer_r * denom_l, denom_l * denom_r]

def main():
	numerator = find_numerator() #find numerator of Nth convergent
	print get_sum_of_digits(numerator) #sum digits of numerator

main()
