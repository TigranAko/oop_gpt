#quadrilateral, rectangle, square
#Bad
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height


def test_area(rectangle: Rectangle):
    rectangle.set_width(10)
    rectangle.set_height(5)
    return rectangle.get_area()

print(test_area(Rectangle(2, 3)))  # Ожидаем 50
print(test_area(Square(2, 3)))  # Логика ломается!


#Ok

from abc import ABC, abstractmethod

class Quadrilateral(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Parallelogram(Quadrilateral):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Recatnagle(Parallelogram):
    pass

class Square(Quadrilateral):
    def __init__(self, length):
        self.length = length

    def set_length(self, length):
        self.length = length

    def get_area(self, length):
        return length*length

def test_area(figure: Parallelogram):
    figure.set_width(10)
    figure.set_height(5)
    return figure.get_area()

print(test_area(Rectangle(2, 3)))  # Ожидаем 50
#print(test_area(Square(2, 3))) # Ошибка обнаруживается при типизации


# BEST

from abc import ABC, abstractmethod

class Quadrilateral(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Parallelogram(Quadrilateral):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Rectangle(Parallelogram):
    pass  # У прямоугольника такая же логика, как у параллелограмма

class Square(Quadrilateral):
    def __init__(self, length):
        self.length = length

    def set_length(self, length):
        self.length = length

    def get_area(self):
        return self.length * self.length

def test_area(figure: Parallelogram):
    figure.set_width(10)
    figure.set_height(5)
    return figure.get_area()

# Тесты
print(test_area(Rectangle(2, 3)))  # Ожидаем 50
# print(test_area(Square(2, 3)))  # Ошибка предотвращена – Square не является Parallelogram

