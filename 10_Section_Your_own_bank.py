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

# to pass the data - name and balance that the user typed in
# x goes up in def __init__ name, amount, min balance

x = Current("Ziyad", 500)
x.deposit(300)
print(x.statement())
# Output: 800 £