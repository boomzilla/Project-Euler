import math

PROMPT = 600851475143

def do_factor(to_factor):
	to_return = [to_factor]

	for n in range(2, int(math.pow(to_factor, 0.5))):
		if (to_factor % n == 0):
			to_return.remove(to_factor)
			to_return.extend(do_factor(to_factor / n))
			to_return.extend(do_factor(n))
			break

	return to_return

def main():
	largest_prime_factor = 1
	factor_list = do_factor(PROMPT)
		
	factor_list.sort()
	factor_list.reverse()

	print factor_list[0]

main()
