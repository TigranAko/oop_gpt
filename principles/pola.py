class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        self.balance -= 10  # Нарушение POLA – метод не должен изменять объект!
        return self.balance


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def get_balance_with_commission(self):
        self.balance -= 10
        return self.balance
