#Device – базовый класс с __init__(), который принимает brand (бренд устройства).
#Mobile – наследуется от Device, добавляет call(), который печатает "Звонок с телефона <brand>".
#Computer – наследуется от Device, добавляет compute(), который печатает "Вычисления на <brand>".
#Smartphone – наследуется от Mobile и Computer, добавляет __init__() и вызывает super().

class Device:
    def __init__(self, brand: str):
        self.brand = brand

class Mobile(Device):
    def __init__(self, brand: str):
        super().__init__(brand)

    def call(self):
        print(f"Звонок с телефона {self.brand}")

class Computer(Device):
    def __init__(self, brand: str):
        super().__init__(brand)

    def compute(self):
        print(f"Вычисления на {self.brand}")

class Smartphone(Mobile, Computer):
    def __init__(self, brand: str):
        super().__init__(brand)



#Проверка:
iphone = Smartphone("Apple")
iphone.call()       # "Звонок с телефона Apple"
iphone.compute()    # "Вычисления на Apple"
