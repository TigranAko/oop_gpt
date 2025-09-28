#Задание: Контроль структуры класса через метакласс
#Описание:
#Создай метакласс, который будет запрещать создание классов без обязательных атрибутов id и метода display_info().

#Если какой-то класс не содержит их, выбрасывай исключение TypeError во время его определения.

#Шаги:
#Создай метакласс CheckClassStructure, который будет проверять, что у создаваемого класса есть:
#Атрибут id (можно задать как None по умолчанию).
#Метод display_info().
#Если чего-то не хватает — вызывай TypeError с пояснением.
#Применяй этот метакласс к новым классам.
#Пример кода:
#python
#Копировать код

class CheckClassStructure(type):
    def __new__(cls, name, parents, namespace):
        print(f"Используется метакласс для {name}")
        if not (namespace.get("id", False) or namespace.get("display_info", False)):
            raise TypeError(f"Класс {name} не может быть создан, так как не соответствует требованиям. Он должен содеражать id и display_info")
        elif not isinstance(namespace.get("id"), int):
            raise ValueError("id должен быть типа int")
        print("создаётся успешно и работает")
        return super().__new__(cls, name, parents, namespace)
    # Твой код здесь

class ValidClass(metaclass=CheckClassStructure):
    id = 1

    def display_info(self):
        print("Этот класс корректен!")

class InvalidClass(metaclass=CheckClassStructure):
    pass  # Здесь нет id и display_info(), значит, должна быть ошибка

obj = ValidClass()  # Работает
obj.display_info()

obj2 = InvalidClass()  # Должна быть ошибка TypeError

#Ожидаемый результат:
#ValidClass создаётся успешно и работает.
#InvalidClass не может быть создан, так как не соответствует требованиям.
#Дополнительно: Если справишься с базовой задачей, можешь расширить метакласс, чтобы проверять, что id — это число (int).
