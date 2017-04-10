'''
Create a class PrimeChecker(number), that takes in
 a string argument. When the instance of the class 
is called with .is_prime() it should return true if
 number is a prime number and false if it isn't.
 '''

class PrimeCheckerI(object):

	#initialize class and attributes
	def __init__(self, number):
		self.number = number

	def is_prime(self):
		num = int(self.number)
		if num == 2:
			return True 

		else:
			for i in range(2, num):
				if num % i == 0:
					return False 
			return True