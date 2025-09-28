#Класс MobilePhone должен иметь свойства: brand, model, screen_size, battery, camera.
#Абстрактный класс Builder должен иметь методы для установки каждого свойства.
#Создайте два класса-строителя: SmartphoneBuilder и FeaturePhoneBuilder, которые задают конкретные значения для каждого типа телефона.
#Класс Director должен управлять процессом построения двух видов телефонов: смартфона и кнопочного телефона.
#После сборки, объект MobilePhone должен выводить свои характеристики через метод __str__.
#Пример использования
from abc import ABC
class MobilePhone:
    def __init__(self):
        self.brand = None
        self.model = None
        self.screen_size = None
        self.battery = None
        self.camera = None
    
    def set_property(self, name, value):
        print(self, name, value)
        setattr(self, name, value)

    def __str__(self):
        return f"MobilePhone {self.brand=} {self.model=} {self.screen_size=} {self.battery=} {self.camera=}"

class Builder:
    def __init__(self):
        self.phone = MobilePhone()

    def set_brand(self, brand):
        print(1)
        self.phone.set_property("brand", brand)
        print(2)
    def set_model(self, brand):
        self.phone.set_property("model", brand)

    def set_screen_size(self, brand):
        self.phone.set_property("screen_size", brand)
    def set_battery(self, brand):
        self.phone.set_property("battery", brand)
    def set_camera(self, brand):
        self.phone.set_property("camera", brand)


class SmartphoneBuilder(Builder):

    pass
class FeaturePhoneBuilder(Builder):
    pass

class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_smartphone(self):
        return self.build()

    def build(self):
        print(3, self.builder.phone.__dict__)
        self.builder.set_brand = "a"
        print(4)
        self.builder.set_model = "b"
        self.builder.set_screen_size = "c"
        self.builder.set_battery = "d"
        self.builder.set_camera = "e"
        return self.builder.phone

    def build_feature_phone(self):
        return self.build()

director = Director(SmartphoneBuilder())
smartphone = director.build_smartphone()
print(smartphone)
# Должно вывести характеристики смартфона

director = Director(FeaturePhoneBuilder())
feature_phone = director.build_feature_phone()
print(feature_phone)
# Должно вывести характеристики кнопочного телефона




class MobilePhone:
    def __init__(self):
        self.brand = None
        self.model = None
        self.screen_size = None
        self.battery = None
        self.camera = None

    def set_property(self, name, value):
        setattr(self, name, value)

    def __str__(self):
        return (f"MobilePhone(brand={self.brand}, model={self.model}, "
                f"screen_size={self.screen_size}, battery={self.battery}, camera={self.camera})")


class Builder:
    def __init__(self):
        self.phone = MobilePhone()

    def set_brand(self, brand):
        self.phone.set_property("brand", brand)
        return self

    def set_model(self, model):
        self.phone.set_property("model", model)
        return self

    def set_screen_size(self, screen_size):
        self.phone.set_property("screen_size", screen_size)
        return self

    def set_battery(self, battery):
        self.phone.set_property("battery", battery)
        return self

    def set_camera(self, camera):
        self.phone.set_property("camera", camera)
        return self

    def build(self):
        return self.phone


class SmartphoneBuilder(Builder):
    def build(self):
        return (self.set_brand("BrandX")
                    .set_model("X100")
                    .set_screen_size("6.5 inch")
                    .set_battery("4000mAh")
                    .set_camera("48MP")
                    .phone)


class FeaturePhoneBuilder(Builder):
    def build(self):
        return (self.set_brand("BrandY")
                    .set_model("Y200")
                    .set_screen_size("2.4 inch")
                    .set_battery("1000mAh")
                    .set_camera("5MP")
                    .phone)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_phone(self):
        return self.builder.build()


# Создание смартфона
director = Director(SmartphoneBuilder())
smartphone = director.build_phone()
print(smartphone)
# MobilePhone(brand=BrandX, model=X100, screen_size=6.5 inch, battery=4000mAh, camera=48MP)

# Создание кнопочного телефона
director = Director(FeaturePhoneBuilder())
feature_phone = director.build_phone()
print(feature_phone)
# MobilePhone(brand=BrandY, model=Y200, screen_size=2.4 inch, battery=1000mAh, camera=5MP)

