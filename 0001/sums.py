def main():
	def add(x,y): return x+y

	def f(x): return x % 3 == 0 or x % 5 == 0

	print reduce(add, filter(f, range(0, 1000)))

main()
