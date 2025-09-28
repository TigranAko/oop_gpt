#Создай классы устройств: Computer, Smartphone.

#Создай классы ОС: Windows, Linux, Android, iOS.

#Свяжи их через Bridge, чтобы каждое устройство могло работать с разными ОС.

#Реализуй метод run(), который будет выводить, какое устройство работает на какой ОС.

#Computer running Windows  
#Smartphone running Android  

class Device:
    def __init__(self, system):
        self.system = system

    def run(self):
        return f"{self.__class__.__name__} running {self.system.__class__.__name__}"

class Computer(Device):
    pass

class Smartphone(Device):
    pass

    
class System:
    pass

class Windows(System):
    pass

class Linux(System):
    pass

class Android(System):
    pass

class IOS(System):
    pass


android = Android()
computer = Computer(android)
print(computer.run())





class Device:
    def __init__(self, system):
        self.system = system

    def run(self):
        return f"{self.__class__.__name__} running {self.system.name()}"


class Computer(Device):
    pass

class Smartphone(Device):
    pass


class System:
    def name(self):
        return self.__class__.__name__

    def run(self):
        return f"Running {self.name()}"


class Windows(System):
    pass

class Linux(System):
    pass

class Android(System):
    pass

class IOS(System):
    pass


# Тестируем
windows = Windows()
android = Android()

computer = Computer(windows)
phone = Smartphone(android)

print(computer.run())  # "Computer running Windows"
print(phone.run())     # "Smartphone running Android"

