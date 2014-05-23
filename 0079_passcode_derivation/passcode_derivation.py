#Solution to Project Euler 79 by Ian Ruotsala

PATH = "/home/ian/Documents/prog/projectEuler/0079_passcode_derivation/"
FILE = "keylog.txt"

def main():
	string_set = set()
	f = open(PATH + FILE, "r")
	for line in f.readline():
		temp_set = add_digits(string_set, line)
		string_set.clear()
		string_set = minimize(temp_set)
	print string_set
main()
