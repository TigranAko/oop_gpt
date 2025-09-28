class Oil:
    def __init__(self, level):
        self.level = level  # Уровень масла в двигателе

class Engine:
    def __init__(self, oil):
        self.oil = oil  # Объект Oil

class Car:
    def __init__(self, engine):
        self.engine = engine  # Объект Engine

    def check_oil_level(self):
        return self.engine.oil.level  # Нарушение LoD (обращаемся к oil через engine)



class Oil:
    def __init__(self, level):
        self.level = level  # Уровень масла в двигателе

class Engine:
    def __init__(self, oil):
        self.oil = oil  # Объект Oil

    def get_oil_level(self):
        return self.oil.level

class Car:
    def __init__(self, engine):
        self.engine = engine  # Объект Engine

    def check_oil_level(self):
        return self.engine.get_oil_level()

