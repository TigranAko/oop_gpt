class City:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    def move_to(self, new_city):
        self.city = new_city

    def get_city(self):
        return self.city.name

moscow = City("Moscow")
erevan = City("Erevan")

artem = Person("Artem", moscow)
artem.move_to(erevan)
print(artem.get_city())
