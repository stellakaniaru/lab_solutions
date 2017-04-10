class BankAccount(object):
	def __init__(self, balance = 0.0):
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeError('invalid transaction')
		self.balance -= amount
		return self.balance

class MinimumBalanceAccount(BankAccount):
	pass