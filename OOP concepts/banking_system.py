class Customer:
    def __init__(self, name, email, customer_id):
        self._name = name
        self._email = email
        self._customer_id = customer_id

    def customer_info(self):
        return f"Name: {self._name}, email: {self._email}"

    def change_name(self, new_name):
        self._name = new_name

    def change_email(self, new_email):
        self._email = new_email


class BankAccount:
    def __init__(self, balance, owner, account_number):
        self._balance = balance
        self._owner = owner
        self._account_number = account_number

    def refill(self, num):
        if num>0:
            self._balance += num
            return self._balance
        return "Amount should be greater than 0."

    def withdrawal(self, num):
        if num <= self._balance:
            self._balance = self._balance - num
            return self._balance
        return "Insufficient funds"

    def get_account_number(self):
        return f"Account number - {self._account_number}"


first_user = Customer("Tom", "tom@gmail.com", 123)
print(first_user.customer_info())
first_user.change_name("Jack")
first_user.change_email("jack@gmail.com")
print(first_user.customer_info())

current_account = BankAccount(500, first_user, 321)
print(current_account.refill(1000))
print(current_account.withdrawal(200))
