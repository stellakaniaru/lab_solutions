class Counter(object):
	number = 0
	def __init__(self):
		type(self).number += 1

	def __del__(self):
		type(self).number -= 1


class Account(Counter):

	def __init__(self, holder, number, balance, credit_line = 1500):
		Counter.__init__(self)
		
		self.Holder = holder
		self.Number = number
		self.Balance = balance
		self.CreditLine = credit_line

	def transfer(self, target, amount):
		if(self.Balance - amount < - self.CreditLine):
			#coverage insufficient
			return False
		else:
			self.Balance -= amount
			target.Balance += amount
			return True

	def deposit(self, amount):
		self.Balance = amount

	def withdraw(self, amount):
		if(self.Balance - amount < - self.CreditLine):
			#coverage insufficient
			return False
		else:
			self.Balance -= amount
			return True


	def balance(self):
		return self.Balance





