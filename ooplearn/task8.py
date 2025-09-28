#Создай метакласс SingletonMeta, который хранит единственный экземпляр в атрибуте класса.
#В __call__() проверяй, существует ли уже объект. Если да — возвращай его. Если нет — создавай новый.
class SingletonMeta(type):
    # Реализация паттерна Singleton
    singlecls = None
    _instance = {}
#    def __new__(cls, name, parents, namespace):
#        print("new")
#        if not cls.singlecls:
#            cls.singlecls = cls
#            return super().__new__(cls, name, parents, namespace)
#        return super().__new__(cls.singlecls, name, parents, namespace)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]

        print("call", self.singlecls, id(self.singlecls))
        if not self.singlecls:
            self.singlecls = self
            print(self.singlecls, id(self.singlecls), id(self.singlecls()), id(self), id(super().__call__))
            return self.singlecls 
            return super().__call__()
        return self.singlecls


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("Создан объект Logger")

# Проверка:
logger1 = Logger()
logger2 = Logger()

print(id(logger1), id(logger2))
print(logger1 is logger2)  # Должно вывести: True
#Ожидаемый результат:
#При первом вызове Logger() создаётся объект.
#При втором вызове Logger() новый объект не создаётся, а возвращается старый.
#Вывод print(logger1 is logger2) должен быть True.
