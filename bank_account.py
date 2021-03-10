# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f'Interest Rate: {self.int_rate}, Balance:${self.balance}')
        return self

    def yield_interest(self):
        self.balance *= self.int_rate
        return self

account1 = BankAccount(0.06, 2000)

account1.deposit(300).deposit(600).deposit(1000).withdraw(700).yield_interest().display_account_info()

account2 = BankAccount(0.08, 4000)

account2.deposit(1700).deposit(900).withdraw(450).withdraw(50).withdraw(150).withdraw(60).yield_interest().display_account_info()