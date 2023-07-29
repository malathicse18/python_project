# Mini Bank Application

class Customer:
    """
    This Class Developed By Malathi and Describes Bank Operators
    """
    bank_name = 'HDFC BANK'

    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):          # INSTANCE METHOD
        self.balance = self.balance + amount
        print('After deposit balance: ', self.balance)

    def withdraw(self, amount):         # INSTANCE METHOD
        if amount > self.balance:
            print('Insufficient Funds, cannot perform this transaction')
        else:
            self.balance = self.balance - amount
            print('After withdraw, balance: ', self.balance)

print('Welcome to', Customer.bank_name)
name = input('Enter Your Name: ')
c = Customer(name)
while True:
    print('D - Deposit \n W - Withdrawal \n E - Exit')
    option = input('Choose your option')
    if option.lower() == 'd':
        amount = float(input('Enter amount to deposit: '))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount to withdraw: '))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for banking with us')
        break
    else:
        print('Your option is invalid, please chose valid option to proceed.')

