class User():

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    
    def make_deposit(self, ammount):
        self.balance += ammount
    
    def make_withdrawal(self, ammount):
        self.balance -= ammount
    
    def display_user_balance(self):
        print(f'User: ' + self.name + ', Balance: $' + str(self.balance))

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f'$' + str(amount) + ' from ' + self.name + ' to ' + other_user.name + ' has been transfered!')
        self.display_user_balance()
        other_user.display_user_balance()

dan = User('Daniyar', 'daniyar@gmail.com')
natalie = User('Natalie', 'natalie@gmail.com')
frank = User('Frank', 'frank@gmail.com')

dan.make_deposit(1000)
dan.make_deposit(15000)
dan.make_deposit(250)
dan.make_withdrawal(145)
dan.display_user_balance()

natalie.make_deposit(25000)
natalie.make_deposit(3450)
natalie.make_withdrawal(400)
natalie.make_withdrawal(120)
natalie.display_user_balance()

frank.make_deposit(10000)
frank.make_withdrawal(320)
frank.make_withdrawal(480)
frank.make_withdrawal(1020)
frank.display_user_balance()

dan.transfer_money(frank, 10000)