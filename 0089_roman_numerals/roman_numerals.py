#solution for Project Euler prompt 89, by Ian Ruotsala

PATH = "/home/ian/Documents/prog/projectEuler/0089_roman_numerals/"
FILE_NAME = "roman.txt"

def arabic_to_roman(aint):
	to_return = ""

	thousand_factor = aint / 1000
	to_return += "M" * thousand_factor
	aint %= 1000

	if (aint / 900) > 0:
		to_return = "CM" + to_return
		aint %= 900

	if (aint / 500) > 0:
		to_return += "D"
		aint %= 500
	elif (aint / 400) > 0:
		to_return += "CD"
		aint %= 400

	hundred_factor = aint / 100
	to_return += "C" * hundred_factor
	aint %= 100

	#this will produce out-of-order subtractrive pairs
	#however, they will still be of correct length
	if (aint / 90) > 0:
		to_return = to_return + "XC"
		aint %= 90

	if (aint / 50) > 0:
		to_return += "L"
		aint %= 50
	elif (aint / 40) > 0:
		to_return += "XL"
		aint %= 40

	ten_factor = aint / 10
	to_return += "X" * ten_factor
	aint %= 10

	if (aint / 9) > 0:
		to_return = to_return + "IX"
		aint %= 9

	if (aint / 5) > 0:
		to_return += "V"
		aint %= 5
	elif (aint / 4) > 0:
		to_return += "IV"
		aint %= 4

	to_return += "I" * aint

	return to_return

def parse_rom_num(rom_num):
	rom_num = rom_num.lower()
	to_return = 0
	previous_char = "" #remember previous character is case of subtractive pairs
	for char in rom_num:
		if char == "m":
			if previous_char == "c":
				to_return += 800
			else:
				to_return += 1000
		elif char == "d":
			if previous_char == "c":
				to_return += 300
			else:
				to_return += 500
		elif char == "c":
			if previous_char == "x":
				to_return += 80
			else:
				to_return += 100
		elif char == "l":
			if previous_char == "x":
				to_return += 30
			else:
				to_return += 50
		elif char == "x":
			if previous_char == "i":
				to_return += 8
			else: 
				to_return += 10
		elif char == "v":
			if previous_char == "i":
				to_return += 3
			else:
				to_return += 5
		else:
			#case char == "i"
			to_return += 1
		previous_char = char
	return to_return

def test():
	print parse_rom_num("i") #1
	print parse_rom_num("III") #3
	print parse_rom_num("V") #5
	print parse_rom_num("CM") #900
	print parse_rom_num("cMMxcix") #1999

	print arabic_to_roman(5000) + "= MMMMM?"
	print arabic_to_roman(4900) + "= CMMMMM?"
	print arabic_to_roman(900) + "= CM?"
def main():
	test()
	f = open(PATH + FILE_NAME, 'r')
	non_min_count = 0
	min_count = 0
	for line in f.readlines():
		aint = parse_rom_num(line)
		print line + " = " + str(aint)
		non_min_count += len(line)
		min_count += len(arabic_to_roman(aint))

	print (non_min_count - min_count)
main()
