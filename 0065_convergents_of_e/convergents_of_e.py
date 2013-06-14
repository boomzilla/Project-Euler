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

def add_fractions(numer_l, denom_l, numer_r, denom_r):
	#sum two fractions, return resultant numerator and denominator as a list of two items: [numer, denom]
	return [numer_l * denom_r + numer_r * denom_l, denom_l * denom_r]

def div_fractions(numer_top, denom_top, numer_bottom, denom_bottom):
	#divide top fraction by bottom fraction, return resultant numerator and denominator as list of two items: [numer, denom]
	return [numer_top * denom_bottom, numer_bottom * denom_top]

def find_gcd(a, b):
	#find greatest common denominator of two ints
	while (b != 0):
		t = b
		b = a % t
		a = t
	return a

def find_numerator():
	#find the numerator of the Nth convergent, return it
	numerator = 0
	denominator = 0

	for n in range(N_CONV, 0, -1):
		numer_to_add = 1
		denom_to_add = 1
		if (n % 3 == 0):
			denom_to_add = (n * 2) / 3
		if numerator == 0:
			numerator = numer_to_add
			denominator = denom_to_add
		elif (n != 1):
			new_denom = add_fractions(denom_to_add, 1, numerator, denominator)
			result = div_fractions(numer_to_add, 1, new_denom[0], new_denom[1])
			gcd_result = find_gcd(result[0], result[1])
			numerator = result[0]/gcd_result
			denominator = result[1]/gcd_result
		else:
			numerator += (2 * denominator)
	return numerator

def get_sum_of_digits(number):
	#get sum of a series of digits in a number, e.g. 252 would return 9, 4444 would return 16, etc
	result = number % 10
	while (number / 10 != 0):
		number /= 10
		result += number % 10
	return result

def main():
	numerator = find_numerator() #find numerator of Nth convergent
	print get_sum_of_digits(numerator) #sum digits of numerator

main()
