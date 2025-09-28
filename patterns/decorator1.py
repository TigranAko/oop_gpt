#Создай базовый класс Beverage с методом cost() и description().

#Сделай конкретный класс Coffee, который возвращает цену 100 и описание "Coffee".

#Сделай декораторы:

#MilkDecorator — добавляет 20 к цене и описание " + Milk".

#SugarDecorator — добавляет 10 к цене и описание " + Sugar".
class Beverage:
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def cost(self):
        return self._cost

    def description(self):
        return self._description

class Coffee(Beverage):
    def __init__(self, description="Coffee", cost=100):
        super().__init__(description, cost)

class MilkDecorator:
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 20

    def description(self):
        return self.beverage.description() + " + Milk"
        

class SugarDecorator:
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        return self.beverage.cost() + 10

    def description(self):
        return self.beverage.description() + " + Sugar"
        
    
    

coffee = Coffee()
print(coffee.description(), coffee.cost())  # Coffee 100

milk_coffee = MilkDecorator(coffee)
print(milk_coffee.description(), milk_coffee.cost())  # Coffee + Milk 120

sweet_milk_coffee = SugarDecorator(milk_coffee)
print(sweet_milk_coffee.description(), sweet_milk_coffee.cost())  # Coffee + Milk + Sugar 130



from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self, description: str, cost: int):
        self._description = description
        self._cost = cost  

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class Coffee(Beverage):
    def __init__(self):
        super().__init__("Coffee", 100)

    def cost(self):
        return self._cost

    def description(self):
        return self._description

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage, extra_description: str, extra_cost: int):
        super().__init__(beverage.description() + extra_description, beverage.cost() + extra_cost)
        self.beverage = beverage

    def cost(self):
        return self._cost

    def description(self):
        return self._description

class MilkDecorator(BeverageDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, " + Milk", 20)

class SugarDecorator(BeverageDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage, " + Sugar", 10)

coffee = Coffee()
print(coffee.description(), coffee.cost())  # Coffee 100

milk_coffee = MilkDecorator(coffee)
print(milk_coffee.description(), milk_coffee.cost())  # Coffee + Milk 120

sweet_milk_coffee = SugarDecorator(milk_coffee)
print(sweet_milk_coffee.description(), sweet_milk_coffee.cost())  # Coffee + Milk + Sugar 130

