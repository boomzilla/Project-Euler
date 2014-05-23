#Solution to Project Euler 79 by Ian Ruotsala

PATH = "/home/ian/Documents/prog/projectEuler/0079_passcode_derivation/"
FILE = "keylog.txt"

def add_digits(string_set, line):
	to_return = set()
	for a_string in string_set:
		to_return = to_return.union(join_strings(line, a_string))
	if len(to_return) == 0:
		to_return.add(line)
	return to_return

#pre: assume three_digits has no matching chars
def join_strings(three_digits, large_string):
	to_return = set()
	for a in range(len(large_string)):
		for b in range(a,len(large_string)):
			for c in range(b,len(large_string)):
				insert_string = ""
				if (three_digits[0] == large_string[a]):
					insert_string += large_string[0:a] + three_digits[0] + large_string[a+1:b]
				else:
					insert_string += large_string[0:a] + three_digits[0] + large_string[a:b]
				if (three_digits[1] == large_string[b]):
					insert_string += three_digits[1] + large_string[b+1:c]
				else:
					insert_string += three_digits[1] + large_string[b:c]
				if (three_digits[2] == large_string[c]):
					insert_string += three_digits[2] + large_string[c+1:]
				else:
					insert_string += three_digits[2] + large_string[c:]
				to_return.add(insert_string)
	#print to_return
	#raw_input()
	return to_return

def minimize(temp_set):
	to_return = set()
	min_len = -1
	for elem in temp_set:
		if (len(elem) < min_len or min_len == -1):
			#print elem
			min_len = len(elem)
	remove_set = set()
	for elem in temp_set:
		if len(elem) > min_len:
			#print "remove " + str(len(elem)) + " " + str(min_len)
			#print len(elem)
			#print min_len
			remove_set.add(elem)
	#print temp_set
	#print remove_set
	to_return = temp_set.difference(remove_set)
	#temp_iter = temp_set.__iter__()
	#to_return = to_return.union(temp_set)
	#print temp_set
	#print to_return
	return to_return

def main():
	string_set = set()
	f = open(PATH + FILE, "r")
	for line in f.readlines():
		print line
		temp_set = add_digits(string_set, line[0:3])
		#print temp_set
		string_set.clear()
		string_set = minimize(temp_set)
		#print string_set
	print string_set
main()
