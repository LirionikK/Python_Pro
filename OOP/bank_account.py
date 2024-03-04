class BankAccount:
    def __init__(self, balance) -> None:
        self.balance = balance

    def __str__(self) -> str:
        return f"You account balance is: {self.balance}"

    def withdraw(self, num):
        if num > self.balance:
            raise TypeError("Insufficient funds")
        else:
            self.balance -= num

    def topup(self, num):
        self.balance += num


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)
