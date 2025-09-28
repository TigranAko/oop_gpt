class Discount:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def apply_discount(self, price):
        if self.type == "percent":
            return price * (1 - self.value / 100)
        elif self.type == "fixed":
            return price - self.value
        else:
            raise ValueError("Invalid discount type")

# BAD CODE ^

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass
        #raise ValueError("Invalid discount type")


class DiscountPercent(Discount):
    @staticmethod
    def apply_discount(price, value):
        return price * (1 - value / 100)


class DiscountFixed(Discount):
    @staticmethod
    def apply_discount(price,  value):
        return price - value

class Product:
    def __init__(self, price: int|float, discount_type: Discount, value: int | float):
        self.price = price
        self.discount = discount_type # Тип скидки
        self.value = value # Размер скидки

    def __str__(self):
        return f"Price with discount: {self.discount.apply_discount(self.price, self.value)}"


laptop = Product(30000, DiscountFixed(), 5000)
print(laptop)

class Product2:
    def __init__(self, price: int|float, discount_type: Discount, value: int | float):
        self.price = discount_type.apply_discount(price, value)

    def __str__(self):
        return f"price with discount: {self.price}"

computer = Product2(50000, DiscountPercent, 10)
print(computer)

# Best code \/

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class DiscountPercent(Discount):
    def __init__(self, value: float):
        self.value = value

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.value / 100)


class DiscountFixed(Discount):
    def __init__(self, value: float):
        self.value = value

    def apply_discount(self, price: float) -> float:
        return price - self.value


class Product:
    def __init__(self, price: float, discount: Discount):
        self.price = price
        self.discount = discount

    def get_final_price(self) -> float:
        return self.discount.apply_discount(self.price)

    def __str__(self):
        return f"Price with discount: {self.get_final_price()}"


# Использование
laptop = Product(30000, DiscountFixed(5000))
print(laptop)  # Price with discount: 25000

computer = Product(50000, DiscountPercent(10))
print(computer)  # Price with discount: 45000

