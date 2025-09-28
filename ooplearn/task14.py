#Создай дескриптор RangeNumber, который:
#
#Проверяет, чтобы число находилось в заданном диапазоне [min_value, max_value].
#Если число выходит за пределы диапазона, выбрасывает ValueError.
#Если передано не число, выбрасывает TypeError.
#Применить этот дескриптор к классу Product, чтобы проверять:
#
#price — цена товара (должна быть от 1 до 100_000).
#quantity — количество товара (от 0 до 10_000).

class RangeNumber:
    def __init__(self, minimum, maximum, title):
        self.min = minimum
        self.max = maximum
        self.title = title

    def __get__(self, instance, owner):
        return getattr(instance, self.title)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.title, value)

    def verify(self, value):
        if not isinstance(value, int):
            raise TypeError("Значение должно быть типа int")
        elif not self.min <= value <= self.max:
            raise ValueError(f"Значение должно быть в диапазоне [{self.min}, {self.max}]")
        return True




class Product:
    price = RangeNumber(1, 100000, "_price")
    quantity = RangeNumber(0, 10000, "_quantity")

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity


p = Product("Ноутбук", 50000, 5)
print(p.price)  # 50000
print(p.quantity)  # 5

p.price = 120000  # ValueError: Значение должно быть в диапазоне [1, 100000]
p.quantity = -1   # ValueError: Значение должно быть в диапазоне [0, 10000]
