class Account:
    def __init__(self, balance=0):
        self._balance = balance
        self._account_holder = None

    def get_balance(self):
        return self._balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            self._balance = value
        else:
            print("Error: Balance must be greater than 0.")

    @property
    def account_holder(self):
        return self._account_holder

    @account_holder.setter
    def account_holder(self, value):
        self._account_holder = value


acc = Account()
print("Initial balance:", acc.get_balance())

acc.balance = 100
print("New balance:", acc.balance)

acc.account_holder = "Mike"
print("Account holder:", acc.account_holder)
