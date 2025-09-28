#Создай метакласс RegistryMeta, который при создании нового класса добавляет его в registered_classes.
#В registered_classes должен храниться словарь {имя_класса: сам_класс}.
#Реализуй несколько классов, использующих этот метакласс.
#Проверь, правильно ли они регистрируются.
#Пример кода:
#python
#Копировать код
class RegistryMeta(type):
    registered_classes = {}

    def __new__(cls, name, bases, namespace):
        cls.registered_classes[name] = super().__new__(cls, name, bases, namespace)
        return super().__new__(cls, name, bases, namespace)
        

class Animal(metaclass=RegistryMeta):
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

print(RegistryMeta.registered_classes)  
# Ожидаемый результат: {'Animal': <class '__main__.Animal'>, 'Dog': <class '__main__.Dog'>, 'Cat': <class '__main__.Cat'>}
#Ожидаемый результат:
#Классы Animal, Dog, Cat автоматически регистрируются в RegistryMeta.registered_classes.
#Вывод print(RegistryMeta.registered_classes) должен показать список всех зарегистрированных классов.
