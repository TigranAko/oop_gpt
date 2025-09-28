#bad
class Printer:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass

    def print_3d_object(self):
        pass

# Ok

class Printer:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass


class Printer3D:
    def print_3d_object(self):
        pass

# best

from abc import ABC, abstractmethod

# Интерфейс для обычной печати
class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass

# Интерфейс для сканирования
class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Интерфейс для факсов
class Faxable(ABC):
    @abstractmethod
    def fax_document(self):
        pass

# Интерфейс для 3D-печати
class Printable3D(ABC):
    @abstractmethod
    def print_3d_object(self):
        pass

# Обычный принтер (только печать)
class BasicPrinter(Printable):
    def print_document(self):
        print("Printing document...")

# Многофункциональный принтер (печать, сканирование, факс)
class MultifunctionPrinter(Printable, Scannable, Faxable):
    def print_document(self):
        print("Printing document...")

    def scan_document(self):
        print("Scanning document...")

    def fax_document(self):
        print("Sending fax...")

# 3D-принтер (только 3D-печать)
class Printer3D(Printable3D):
    def print_3d_object(self):
        print("Printing 3D object...")

# Тесты
printer1 = BasicPrinter()
printer1.print_document()  # Printing document...

printer2 = MultifunctionPrinter()
printer2.print_document()  # Printing document...
printer2.scan_document()   # Scanning document...
printer2.fax_document()    # Sending fax...

printer3 = Printer3D()
printer3.print_3d_object()  # Printing 3D object...

