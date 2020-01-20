# 71. lesson - Make your own bank
# a current account and saving account
# deposit, withdraw, statement
# different minimum limits

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds.")

    def statement(self):
        print("Account balance: £{}".format(self.balance))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = - 1000) 

    def __str__(self):
        return "{}'s Current Account : Balance £{}".format(self.name, self.balance)

# to pass the data - name and balance that the user typed in
# x goes up in def __init__ name, amount, min balance

x = Current("Ziyad", 500)
x.deposit(300)
print(x.statement())
# Output: Account balance: 800 £

x.withdraw(1000)
print(x.statement())
# Output: Account balance: £-200

x.withdraw(1)
# How do I get "not enough funds?!"

x = Current("Ziyad", 500)
print(x)
# Output: Ziyad's Current Account : Balance £500

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance £{}".format(self.name, self.balance) 


x = Current("Ziyad", 500)
y = Savings("Tom", 300)

y.withdraw(300)
y.statement()

y.withdraw(1)
# Output: Sorry, not enough funds.

x.withdraw(1300)
x.statement()

x.withdraw(1)

# 72. lesson - Section review
# classes = templates for object
# objects have states and methods
# learned about inheritence - one big parent class with defined stuff and put
# the stuff from mini child class to the parent class and take care of it

# coins
# polymorph. when we stopped coins from rusting - some still gold

# bank
# __str__ (self) for nice output

# The last coding challenge
print("Goodbye you beautiful people!")