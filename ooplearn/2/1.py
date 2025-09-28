class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        if self.verify_age(age):
            self._age = age
        else:
            print("Ошибка: возраст не может быть отрицательным")

    @classmethod
    def verify_age(cls, age):
        return age>0

    def display_info(self):
        print(f"{self._name}, {self._age} лет")

    @property
    def age()
        return self._age

    @age.setter
    def age(new_age):
        self._age = new_age


class Employee(Person):
    def __init__(self, name: str, age: int, position: str):
        super().__init__(name, age)
        if verify_position:
            self._position = position

    @classmethod
    def verify_position(cls, position):
        if position:                                                        return True
        else:                                                               print("Ошибка должность не может быть пустой")

    def display_info(self):
        print(f"{self._name}, {self._age} лет, работает как {self._position}")
        #super().display_info() + "работает как " + self._position

    def work(self):
        print(f"{self._name} работает на должности {self._position}")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if self.verify_position():
            self._position = new_position


employee = Employee("Алексей", 30, "Менеджер")
employee.display_info()  # Алексей, 30 лет, работает как Менеджер
employee.work()          # Алексей работает на должности Менеджер
employee.age = -5        # Ошибка: возраст не может быть отрицательным
employee.position = ""   # Ошибка: должность не может быть пустой
employee.position = "Developer"
print(employee.position)
