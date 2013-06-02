def is_palindrome(number):
	number_string = str(number)
	palindrome = True
	for n in range(0, len(number_string)):
		if number_string[n] != number_string[(n+1) * -1]:
			palindrome = False
			break
	return palindrome

def main():
	p_list = []
	for m in range(999,100,-1):
		for n in range(999,m-1,-1):
			product = m * n
			if is_palindrome(product):
				p_list.append(product)

	p_list.sort()
	p_list.reverse()
	print p_list[0]

main()
