#Реализуй класс Temperature, который будет использовать дескрипторы для хранения температуры в градусах Цельсия, но при этом:

#Гарантирует, что температура не может быть ниже -273.15 (абсолютный ноль).
#Позволяет автоматически конвертировать температуру в градусы Фаренгейта.
#Требования:
#Используй дескриптор для хранения температуры.
#При попытке установить значение ниже -273.15°C — выбрасывай ValueError.
#Реализуй метод to_fahrenheit(), который возвращает температуру в Фаренгейтах.

class Celsius:
    def __get__(self, instance, owner):
#        print("get", self, instance, owner)
        return instance.celsius

    def __set__(self, instance, value):
#        print("set", self, instance, value)
        if self.verify(value):
            instance.celsius = value

    @staticmethod
    def verify(celsius):
        if celsius < -273.15:
            raise ValueError("Абсолютный ноль")
        return True


class Temperature:
    celsius = Celsius()

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius + 24 # Я не помню формулу



t = Temperature(-10)
print(t.celsius)  # -10
print(t.to_fahrenheit())  # 14.0

t.celsius = 25
print(t.to_fahrenheit())  # 77.0

t.celsius = -300  # Ошибка: Температура не может быть ниже -273.15!
