class User():

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    
    def make_deposit(self, ammount):
        self.balance += ammount
        return self
    
    def make_withdrawal(self, ammount):
        self.balance -= ammount
        return self
    
    def display_user_balance(self):
        print(f'User: ' + self.name + ', Balance: $' + str(self.balance))
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f'$' + str(amount) + ' from ' + self.name + ' to ' + other_user.name + ' has been transfered!')
        self.display_user_balance()
        other_user.display_user_balance()
        return self

dan = User('Daniyar', 'daniyar@gmail.com')
natalie = User('Natalie', 'natalie@gmail.com')
frank = User('Frank', 'frank@gmail.com')

dan.make_deposit(1000).make_deposit(15000).make_deposit(250).make_withdrawal(145).display_user_balance().transfer_money(frank, 10000)
natalie.make_deposit(25000).make_deposit(3450).make_withdrawal(400).make_withdrawal(120).display_user_balance()
frank.make_deposit(10000).make_withdrawal(320).make_withdrawal(480).make_withdrawal(1020).display_user_balance()