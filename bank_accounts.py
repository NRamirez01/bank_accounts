class BankAccount:
    def __init__(self, balance=0, int_rate=0.015):
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self,amount):
        self.balance +=amount
        return self
    def withdrawal(self,amount):
        self.balance -=amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.int_rate * self.balance)
            return self
    @classmethod
        
account_1 = BankAccount(200)
account_2 = BankAccount(900)
account_1.deposit(200).deposit(900).deposit(300).withdrawal(200).yield_interest().display_account_info()
account_2.deposit(50).deposit(50).withdrawal(250).withdrawal(250).withdrawal(250).withdrawal(249).yield_interest().display_account_info()