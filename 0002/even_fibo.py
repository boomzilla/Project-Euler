fibo1 = 0
fibo2 = 1
sum = 0

while (fibo2 < 4000000):
	if fibo2 % 2 == 0:
		sum += fibo2
	temp = fibo2
	fibo2 += fibo1
	fibo1 = temp

print sum
