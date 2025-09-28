#Создай базовый класс Payment с абстрактным методом pay().
#Создай два подкласса: CreditCardPayment и PayPalPayment.
#Реализуй PaymentFactory, который создает нужный объект в зависимости от переданного типа.
#Проверь, что фабрика возвращает правильные объекты.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("pay with credit cart")


class PayPalPayment(Payment):
    def pay(self):
         print("pay with paypal")

class PaymentFactory():
    @staticmethod
    def create_payment(type_):
        if type_=="paypal":
            return PayPalPayment()
        elif type_=="creditcart":
            return CreditCardPayment()

p = PaymentFactory.create_payment("paypal")
p.pay()



from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Paying with credit card")

class PayPalPayment(Payment):
    def pay(self):
        print("Paying with PayPal")

class PaymentFactory:
    @staticmethod
    def create_payment(type_):
        if type_ == "paypal":
            return PayPalPayment()
        elif type_ == "creditcard":  # Исправил "creditcart"
            return CreditCardPayment()
        else:
            raise ValueError(f"Unknown payment type: {type_}")

# Проверка
p1 = PaymentFactory.create_payment("paypal")
p1.pay()  # Paying with PayPal

p2 = PaymentFactory.create_payment("creditcard")
p2.pay()  # Paying with credit card

# p3 = PaymentFactory.create_payment("bitcoin")  # ValueError: Unknown payment type: bitcoin

