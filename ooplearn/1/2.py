
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("first", 1)
dog2 = Dog("second", 2)
dog1.bark()
dog2.bark()
