n = int(input("Number of iterations:\n"))
def wallis(n):
	x = 1
	for i in range(1,n+1):
		x = x*(4*i**2)/(4*i**2-1)
	return x*2
print(wallis(n))
