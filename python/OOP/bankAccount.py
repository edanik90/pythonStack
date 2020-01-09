class BankAccount:
	def __init__(self, interest_rate = 0.02, balance = 0):
		self.balance = balance
		self.interest_rate = interest_rate

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		self.balance -= amount
		if self.balance < 0:
			print('Insufficient funds: Charging a $5 fee')
			self.balance -= 5
		return self

	def display_account_info(self):
		print(f'Balance: $' + str(self.balance))
		return self

	def yield_interest(self):
		if self.balance > 0:
			self.balance += self.balance * self.interest_rate
		return self

account_1 = BankAccount(0.04)
account_2 = BankAccount(0.08)
account_1.deposit(1000).deposit(2000).deposit(3000).withdraw(200).yield_interest().display_account_info()
account_2.deposit(3000).deposit(1400).withdraw(150).withdraw(50).withdraw(30).withdraw(6000).yield_interest().display_account_info()