from math import pi

class Rectangle:
    def __init__(self, width, height):
        self.width = max(0, width) # Если значение отрицательное то используется 0
        self.height = max(0, height)

    def perimeter(self):
        return (self.width+self.height)*2

    def area(self):
        return self.width*self.height

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __str__(self):
        return f"Rectangle(width: {self.width}, height: {self.height})"


class Circle:
    def __init__(self, radius):
        self.radius = max(0, radius) # Еcли значение отрицательное

    def area(self):
        return 2*pi*self.radius

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        return self.area() + other.area()

    def __str__(self):
        return f"Circle(radius: {self.radius})"



r1 = Rectangle(2, 9)
r2 = Rectangle(3, 6)
c1 = Circle(3)
c2 = Circle(3)

print(r1 + r2)  # Сложение площадей прямоугольников
print(c1 + c2)  # Сложение площадей кругов
print(r1 == r2) # Сравнение площадей
print(c1 == c2) # Сравнение площадей

print(r1)  # Вывод информации о прямоугольнике
print(c1)  # Вывод информации о круге

