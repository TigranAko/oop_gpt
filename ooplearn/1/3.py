class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


user = BankAccount(1234_5678_9010_1112, 100)
user.deposit(5000)
user.withdraw(2000)
print(user.balance)


