#Создай базовый класс Pizza, у которого есть:

#Метод cost(), возвращающий базовую стоимость.

#Метод description(), возвращающий название пиццы.

#Реализуй несколько видов пиццы, например: Margherita, Pepperoni.

#Создай декораторы для топпингов:
#
#CheeseDecorator (+30 к стоимости, добавляет " + Cheese").

#OlivesDecorator (+25 к стоимости, добавляет " + Olives").

#BaconDecorator (+40 к стоимости, добавляет " + Bacon").

#Декораторы должны быть вложены друг в друга для комбинирования топпингов.

#Проверь работу кода, создав пиццу и добавив к ней несколько топпингов.
class Pizza:
    _cost = int
    _desc = str

    def cost(self):
        return self._cost

    def description(self):
        return self._desc

class Margherita(Pizza):
    def __init__(self):
        self._cost = 200
        self._desc = "Margherita"


class Pepperoni(Pizza):
    def __init__(self):
        self._cost = 100
        self._desc = "Margherita"


class Decorator:
    def __init__(self, pizza, add_desc='', add_cost=0):
        self.pizza = pizza
        self._cost = self.pizza._cost + add_cost
        self._desc = self.pizza._desc + " + " + add_desc

    def cost(self):
        return self.pizza._cost

    def description(self):
        return self.pizza._desc

class CheeseDecorator(Decorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Cheese", 30)

class BaconDecorator(Decorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Bacon", 50)

class OlivesDecorator(Decorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Olives", 45)


pizza = Margherita()
print(pizza.description(), pizza.cost())  # "Margherita 200"

cheesy_pizza = CheeseDecorator(pizza)
print(cheesy_pizza.description(), cheesy_pizza.cost())  # "Margherita + Cheese 230"

loaded_pizza = BaconDecorator(OlivesDecorator(cheesy_pizza))
print(loaded_pizza.description(), loaded_pizza.cost())  # "Margherita + Cheese + Olives + Bacon 295"



class Pizza:
    def cost(self):
        return 0

    def description(self):
        return ""

class Margherita(Pizza):
    def cost(self):
        return 200

    def description(self):
        return "Margherita"

class Pepperoni(Pizza):
    def cost(self):
        return 220

    def description(self):
        return "Pepperoni"


class Decorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza


class CheeseDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 30

    def description(self):
        return self.pizza.description() + " + Cheese"


class BaconDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 50

    def description(self):
        return self.pizza.description() + " + Bacon"


class OlivesDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 45

    def description(self):
        return self.pizza.description() + " + Olives"


# Примеры
pizza = Margherita()
print(pizza.description(), pizza.cost())  # Margherita 200

cheesy_pizza = CheeseDecorator(pizza)
print(cheesy_pizza.description(), cheesy_pizza.cost())  # Margherita + Cheese 230

loaded_pizza = BaconDecorator(OlivesDecorator(cheesy_pizza))
print(loaded_pizza.description(), loaded_pizza.cost())  # Margherita + Cheese + Olives + Bacon 325

