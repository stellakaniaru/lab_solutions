'''Factorial function that takes in an argument and returns the
factorial of the argument given.'''

def factorial(x):
	fact = 1
	if x > 0:
		if x <= 1:
			return 1

		else:
			for i in range(1, (x + 1)):
				fact *= i
			return fact
	
	else:
		return 'no factorial for negative numbers!'

print factorial(-5)
