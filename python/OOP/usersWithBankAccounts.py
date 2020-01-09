class User():

    def __init__(self, name, email, interest_rate):
        self.interest_rate = interest_rate
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate, balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f'User: ' + self.name + ', ' + self.account.display_account_info())
        return self

    def transfer_money(self, other_user, amount):
        self.account.transfer(other_user, amount)
        print(f"$" + str(amount) + " from " + self.name + "'s account to " + other_user.name + "'s account has been transfered!")
        return self

class BankAccount():
	
    def __init__(self, interest_rate, balance):
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

    def transfer(self, other_user, amount):
        self.other_user = other_user
        self.withdraw(amount)
        other_user.account.deposit(amount)
        self.display_account_info()
        other_user.account.display_account_info()
        return self

    def display_account_info(self):
        return (f'Balance: $' + "% 0.2f " % self.balance)


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self


dan = User('Daniyar', 'daniyar@gmail.com', 0.03)
natalie = User('Natalie', 'natalie@gmail.com', 0.02)
frank = User('Frank', 'frank@gmail.com', 0.02)

dan.make_deposit(1000).make_deposit(15000).make_deposit(250).make_withdrawal(145)
dan.account.yield_interest()
dan.display_user_balance()
natalie.make_deposit(25000).make_deposit(3450).make_withdrawal(400).make_withdrawal(120)
natalie.account.yield_interest()
natalie.display_user_balance()
frank.make_deposit(10000).make_withdrawal(320).make_withdrawal(480).make_withdrawal(1020)
frank.account.yield_interest()
frank.display_user_balance()

dan.transfer_money(frank, 5000).display_user_balance()
frank.display_user_balance()