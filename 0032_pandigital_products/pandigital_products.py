import string

UPPER_LIM = 9875432

def is_pandigital(int_x, int_y, int_z):
	digits = "123456789"
	str_x = str(int_x)
	str_y = str(int_y)
	str_z = str(int_z)
	for dig in digits:
		if (str_x.find(dig) != -1):
			str_x = str_x.replace(dig, "")
		elif (str_y.find(dig) != -1):
			str_y = str_y.replace(dig, "")
		elif (str_z.find(dig) != -1):
			str_z = str_z.replace(dig, "")
		else:
			return False

	#print str_x + str_y + str_z
	if (len(str_x) != 0 or len(str_y) != 0 or len(str_z) != 0):
		return False

	return True

def potential_pandigital(test_int):
	test_str = str(test_int)
	if (test_str.find("0") != -1):
		return False
	for char in "123456789":
		if (string.count(test_str, char) > 1):
			return False
	return True

def test():
	print "testing"
	print "true: " + str(is_pandigital(123,456,789))
	print "false: " + str(is_pandigital(12,-345,6789))
	print "false: " + str(is_pandigital(1,2,3))

def main():
	test()
	mp = [] #potential multiplicands
	for n in range(UPPER_LIM):
		if potential_pandigital(n):
			mp.append(n)
	sum = 0
	for m in range(len(mp)):
		print mp[m]
		for n in range(m+1, len(mp)):
			product = mp[m] * mp[n]
			if is_pandigital(mp[m],mp[n],product):
				sum += product
	print sum

main()
