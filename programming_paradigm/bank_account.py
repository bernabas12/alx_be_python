class BankAccount:
    def __init__(self,account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
        return amount
    def withdraw(self, amount):
        if amount > self.account_balance:
            return None
        else:   
            self.account_balance -= amount
            return amount
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
