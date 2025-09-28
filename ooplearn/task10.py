#Реализуй метакласс LoggingMeta, который автоматически добавляет логирование в каждый метод класса.

#Когда вызывается любой метод класса, в консоль должно выводиться сообщение:
#Вызван метод: <имя_метода> с аргументами: <args>, <kwargs>

#Шаги:
#В LoggingMeta.__new__() пройдись по namespace и найди все методы.
#Оберни их в функцию-декоратор, которая при каждом вызове метода будет печатать лог.
#Создай класс ExampleClass(metaclass=LoggingMeta) с несколькими методами.
#Проверь, что при вызове методов в консоли отображается логирование.

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызван метод {func.__name__} с аргументами: {args[1:]}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

class LoggingMeta(type):
    def __new__(cls, name, bases, namespace):
        # Логирование вызовов методов
        newcls = super().__new__(cls, name, bases, namespace)
        print(cls, name, bases, namespace, '\n', newcls)
        for n in namespace:
            if callable(namespace[n]):
                #namespace[n] = cls.decorator(cls, namespace[n])
                namespace[n] = decorator(namespace[n])
        newcls = super().__new__(cls, name, bases, namespace)
        return newcls

#    def decorator(self, func):
#        def wrapper(*args, **kwargs):
#            print(f"Вызван метод {func} с аргументами: {args}, {kwargs}")
#            return func(*args, **kwargs)
#        return wrapper



class ExampleClass(metaclass=LoggingMeta):
    def hello(self, name):
        print(f"Привет, {name}!")

    def add(self, a, b):
        return a + b


ex = ExampleClass()
ex.hello("Алиса")
ex.add(3, 5)
#Ожидаемый результат:
#plaintext
#Копировать код
#Вызван метод: hello с аргументами: ('Алиса',), {}
#Привет, Алиса!
#Вызван метод: add с аргументами: (3, 5), {}


#TRUE

def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызван метод {func.__name__} с аргументами: {args[1:]}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class LoggingMeta(type):
    def __new__(cls, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value):  # Если это метод
                namespace[attr_name] = decorator(attr_value)

        return super().__new__(cls, name, bases, namespace)


class ExampleClass(metaclass=LoggingMeta):
    def hello(self, name):
        print(f"Привет, {name}!")

    def add(self, a, b):
        return a + b


ex = ExampleClass()
ex.hello("Алиса")  # Должен вывести лог + "Привет, Алиса!"
ex.add(3, 5)  # Должен вывести лог + вернуть 8

