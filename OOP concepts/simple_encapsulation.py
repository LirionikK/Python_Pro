class Account:
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self._account_holder = account_holder

    def get_account(self):
        return self.__balance


account = Account(100, "John")
print(account.get_account())
