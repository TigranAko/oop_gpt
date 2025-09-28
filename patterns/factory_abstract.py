#Реализовать Abstract Factory для системы платёжных сервисов (CreditCard, PayPal, Crypto).
#В системе есть два банка (BankA и BankB), каждый предоставляет свои версии платёжных сервисов.
#У каждого банка должны быть разные реализации платежей (например, разные комиссии).
#Реализовать фабрику, которая выбирает банк и создаёт платёжный сервис.

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, bank):
        self.bank = bank
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment from {self.bank} with amount {amount+amount*0.1}")


class PayPal(Payment):
    def pay(self, amount):
        print(f"Processing paypal payment from {self.bank} with amount {amount+30}")


class Crypto(Payment):
    def pay(self, amount):
        print(f"Processing crypto payment from {self.bank} with amount {amount}")


class BankFactory(ABC):
    @abstractmethod
    def create_payment(self, payment):
        pass

class BankAFactory(BankFactory):
    @staticmethod
    def create_payment(payment):
        if payment=="creditcard":
            return CreditCard("BankA")
        elif payment=="paypal":
            return PayPal("BankA")
        else:
            raise ValueError("Этот банк не может использовать данный способ оплаты")


class BankBFactory(BankFactory):
    @staticmethod
    def create_payment(payment):
        if payment=="crypto":
            return Crypto("BankB")
        elif payment=="paypal":
            return PayPal("BankB")
        else:
            raise ValueError("Этот банк не может использовать данный способ оплаты")
    

bank_factory = BankAFactory()
payment = bank_factory.create_payment("creditcard")
payment.pay(100)  
# Должно вывести что-то вроде "Processing credit card payment from BankA with amount 100"

bank_factory = BankBFactory()
payment = bank_factory.create_payment("paypal")
payment.pay(200)
# "Processing PayPal payment from BankB with amount 200"




from abc import ABC, abstractmethod

# Абстрактный класс платежа
class Payment(ABC):
    def __init__(self, bank):
        self.bank = bank

    @abstractmethod
    def pay(self, amount):
        pass

# Реализации платежей для разных банков
class CreditCardA(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment from {self.bank} with amount {amount + amount * 0.1}")  # 10% комиссия

class PayPalA(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment from {self.bank} with amount {amount + 30}")  # Фиксированная комиссия 30

class CreditCardB(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment from {self.bank} with amount {amount + amount * 0.05}")  # 5% комиссия

class PayPalB(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment from {self.bank} with amount {amount + 20}")  # Фиксированная комиссия 20

class CryptoB(Payment):
    def pay(self, amount):
        print(f"Processing crypto payment from {self.bank} with amount {amount}")  # Без комиссии

# Абстрактная фабрика банка
class BankFactory(ABC):
    @abstractmethod
    def create_payment(self, payment_type):
        pass

# Фабрика для банка A
class BankAFactory(BankFactory):
    def create_payment(self, payment_type):
        if payment_type == "creditcard":
            return CreditCardA("BankA")
        elif payment_type == "paypal":
            return PayPalA("BankA")
        else:
            raise ValueError(f"BankA does not support {payment_type} payment")

# Фабрика для банка B
class BankBFactory(BankFactory):
    def create_payment(self, payment_type):
        if payment_type == "creditcard":
            return CreditCardB("BankB")
        elif payment_type == "paypal":
            return PayPalB("BankB")
        elif payment_type == "crypto":
            return CryptoB("BankB")
        else:
            raise ValueError(f"BankB does not support {payment_type} payment")

# Тесты
bank_factory = BankAFactory()
payment = bank_factory.create_payment("creditcard")
payment.pay(100)
# Должно вывести "Processing credit card payment from BankA with amount 110.0"

bank_factory = BankBFactory()
payment = bank_factory.create_payment("paypal")
payment.pay(200)
# Должно вывести "Processing PayPal payment from BankB with amount 220"

