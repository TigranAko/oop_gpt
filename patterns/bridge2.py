#Есть устройства: InkjetPrinter (струйный принтер) и LaserPrinter (лазерный принтер).

#Есть тип печати: BlackAndWhitePrint (чёрно-белая печать) и ColorPrint (цветная печать).

#Устройство должно уметь выводить тип печати, который оно использует.

#В InkjetPrinter и LaserPrinter должен быть атрибут print_type, который отвечает за тип печати.


class PrintType:
    def name(self):
        return self.__class__.__name__

    def run(self):
        return f"printing in {self.name()}"

class BlackAndWhitePrint(PrintType):
    pass

class ColorPrint(PrintType):
    pass


class Printer:
    def __init__(self, print_type: PrintType):
        self.print_type = print_type

    def name(self):
        return self.__class__.__name__

    def print_document(self):
        return f"{self.name()} printing in {self.print_type.name()}"

class LaserPrinter(Printer):
    pass

class InkjetPrinter(Printer):
    pass


bw = BlackAndWhitePrint()
color = ColorPrint()

printer1 = InkjetPrinter(bw)
printer2 = LaserPrinter(color)

print(printer1.print_document())  # "InkjetPrinter printing in Black and White"
print(printer2.print_document())  # "LaserPrinter printing in Color"

