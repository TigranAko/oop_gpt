class PaymentProcessor:
    def __init__(self, user):
        self.user = user

    def pay(self, amount, method):
        if method == "credit_card":
            print(f"Processing credit card payment for {self.user} in amount {amount}")
        elif method == "paypal":
            print(f"Processing PayPal payment for {self.user} in amount {amount}")
        elif method == "crypto":
            print(f"Processing crypto payment for {self.user} in amount {amount}")
        else:
            raise ValueError("Invalid payment method")

class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.total = sum(item["price"] for item in items)
    
    def complete_order(self, payment_method):
        processor = PaymentProcessor(self.user)
        processor.pay(self.total, payment_method)
        print("Order completed!")




from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, user):
        self.user = user

    @abstractmethod
    def pay(self):
        pass

class CreditCartPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment for {self.user} in amount {amount}")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment for {self.user} in amount {amount}")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Processing crypto payment for {self.user} in amount {amount}")


class Order:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        #self.total = sum(item["price"] for item in items)
        self.total = sum(item for item in items)

    def complete_order(self, payment: Payment):
        processor = payment(self.user)
        processor.pay(self.total)
        print("Order completed!")

o = Order("user", [1,2,3,4,6])
o.complete_order(CryptoPayment)

