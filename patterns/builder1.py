#Задача:
#Создай программу для сборки компьютера.
#
#Напиши класс Computer, который будет иметь следующие свойства:
#
#processor (процессор)
#ram (оперативная память)
#graphics (видеокарта)
#storage (накопитель: HDD или SSD)
#Реализуй Builder для компьютера:
#
#Этот Builder должен позволять поочерёдно задавать каждую часть компьютера (например, метод set_processor(), set_ram() и т.д.).
#В конце должен быть метод build(), который возвращает готовый объект Computer.
#Реализуй класс Director, который:
#
#Принимает Builder.
#Имеет методы для сборки разных вариантов компьютеров:
#OfficeComputer: например, процессор "Intel i5", 8GB RAM, интегрированная видеокарта, HDD 1TB.
#GamingComputer: например, процессор "Intel i7", 16GB RAM, выделенная видеокарта "NVIDIA RTX 3080", SSD 512GB.
#Протестируй:
#
#Создай офисный компьютер и игровой компьютер через Director и выведи их параметры.
#Пример использования (ожидаемое поведение):
#
#python
#Copy code

class Computer:
    def __init__(self):
        self._property = {
                "processor": None,
                "ram": None,
                "graphics": None,
                "storage": None
            }


    def set_property(self, property_name, property_value):
        self._property[property_name] = property_value

    
    def __str__(self):
        return f"Computer with: {self._property}"


class Builder:
    def set_processor(self, processor):
        pass

    def set_ram(self, ram):
        pass

    def set_graphics(self, graphics):
        pass

    def set_storage(self, storage):
        pass

    def build(self):
        pass


class YourComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.set_property("processor", processor)

    def set_ram(self, ram):
        self.computer.set_property("ram", ram)

    def set_graphics(self, graphics):
        self.computer.set_property("graphics", graphics)

    def set_storage(self, storage):
        self.computer.set_property("storage", storage)

    def build(self):
        return self.computer

class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_office_computer(self):
        self.builder.set_processor("Intel i5")
        self.builder.set_ram("8GB RAM")
        self.builder.set_graphics("интегрированная видеокарта")
        self.builder.set_storage("HDD 1TB")
        return self.builder.build()


    def build_gaming_computer(self):
        self.builder.set_processor("Intel i7")
        self.builder.set_ram("16GB RAM")
        self.builder.set_graphics("NVIDIA RTX 3080")
        self.builder.set_storage("SSD 512GB")
        return self.builder.build()


director = Director(YourComputerBuilder())

office_pc = director.build_office_computer()
print(office_pc)  
# Должен показать: processor=Intel i5, ram=8GB, graphics=Integrated, storage=HDD 1TB

gaming_pc = director.build_gaming_computer()
print(gaming_pc)  
# Должен показать: processor=Intel i7, ram=16GB, graphics=NVIDIA RTX 3080, storage=SSD 512GB

