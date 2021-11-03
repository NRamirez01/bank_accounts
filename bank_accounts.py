class BankAccount:
    accounts = []
    def __init__(self, balance=0, int_rate=0.015):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)
    def deposit(self,amount):
        self.balance +=amount
        return self
    def withdrawal(self,amount): #forgot to add this until looking at solution
        if(self.balance-amount) >= 0:
            self.balance -=amount
        else:
            print("Insufficient Funds: Charging $5 Overdraft Fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.int_rate * self.balance)
            return self
    @classmethod #only added this after looking into solution
    def display_all_accounts(cls):
            for account in cls.accounts:
                account.display_account_info()
account_1 = BankAccount(200)
account_2 = BankAccount(900)
account_1.deposit(200).deposit(900).deposit(300).withdrawal(200).yield_interest().display_account_info()
account_2.deposit(50).deposit(50).withdrawal(250).withdrawal(250).withdrawal(250).withdrawal(249).yield_interest().display_account_info()
BankAccount.display_all_accounts()