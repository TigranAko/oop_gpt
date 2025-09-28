#Меню состоит из категорий (например, "Горячие блюда", "Напитки").
#
#Каждая категория может содержать либо блюда, либо другие подкатегории.
#
#Блюдо содержит название и цену.
#
#Метод show() должен выводить меню в иерархическом виде.

from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def show(indent=0):
        pass

class Category(MenuItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, item: MenuItem):
        self.children.append(item)

    def show(self, indent=0):
        vidget = '📋' if indent == 0 else '📂'
        print(f"{indent*' '}{vidget} {self.name}")
        for child in self.children:
            child.show(indent+4)

class Dish(MenuItem):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self, indent=0):
        print(f" {indent*' '}🍽 {self.name} - {self.price}")





menu = Category("Меню")
hot_food = Category("Горячие блюда")
drinks = Category("Напитки")

hot_food.add(Dish("Пицца", 500))
hot_food.add(Dish("Борщ", 300))

drinks.add(Dish("Чай", 100))
drinks.add(Dish("Кофе", 150))

menu.add(hot_food)
menu.add(drinks)

menu.show()
#Ожидаемый вывод:
#
#markdown
#Copy code
#📋 Меню
#    📂 Горячие блюда
#        🍽 Пицца - 500 руб.
#        🍽 Борщ - 300 руб.
#    📂 Напитки
#        🍽 Чай - 100 руб.
#        🍽 Кофе - 150 руб.
#Попробуй реализовать!
#







