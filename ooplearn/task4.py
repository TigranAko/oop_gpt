from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Метод должен быть переопределён в подклассах")

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Метод должен быть переопределён в подклассах")

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area() == other.area()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Shape):
            return self.area() + other.area()
        return NotImplemented

    def __str__(self):
        return "Фигура"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = max(0, width)
        self.height = max(0, height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width: {self.width}, height: {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = max(0, radius)

    def area(self):
        return pi * self.radius**2  # Исправленная формула площади круга

    def perimeter(self):
        return 2 * pi * self.radius  # Добавил периметр (длину окружности)

    def __str__(self):
        return f"Circle(radius: {self.radius})"

class Triangle(Shape):
    def __init__(self, a, b ,c):
        if self.verify_triangle(a, b, c):
            self.a = max(0, a)
            self.b = max(0, b)
            self.c = max(0, c)
        else:
            self.a = self.b = self.c = 0

    @classmethod
    def verify_triangle(cls, a, b, c):
        return all((a+b>c, a+c>b, b+c>a))

    def area(self):                                     
        p = self.perimeter()/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2) 

    def perimeter(self):
        return self.a + self.b + self.c  # Добавил периметр (длину окружности)                                          

    def __str__(self):
        return f"Triangle(a: {self.a}, b: {self.b}, c: {self.c})"

# Тестирование
r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)
c1 = Circle(3)
c2 = Circle(4)

print(r1 + r2)  # Сложение площадей прямоугольников
print(c1 + c2)  # Сложение площадей кругов
print(r1 == r2) # Сравнение площадей
print(c1 == c2) # Сравнение площадей

print(r1)  # Вывод информации о прямоугольнике
print(c1)  # Вывод информации о круге

#s = Shape() # ERROR    
r = Rectangle(4, 5)
c = Circle(3)
t = Triangle(3, 4, 5)

print(r.area())  # 20
print(c.area())  # 28.27...
print(t.area())  # 6.0

print(r + c)  # Сложение площадей
print(r == t) # Сравнение площадей

print(t.perimeter())  # 12
print(t)  # Triangle(a: 3, b: 4, c: 5)

