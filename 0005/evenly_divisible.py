DIV_RANGE = 20

def main():
	found_answer = False
	test_number = DIV_RANGE

	while not (found_answer):
		for n in range(1,DIV_RANGE+1):
			if test_number % n != 0:
				break
			if n == DIV_RANGE:
				found_answer = True
				print test_number
		test_number += DIV_RANGE

main()
