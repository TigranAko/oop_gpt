#Flyable – класс с методом fly(), который печатает "Я умею летать!"
#Swimmable – класс с методом swim(), который печатает "Я умею плавать!"
#Bird – класс, который наследуется от Flyable. В Bird добавь метод chirp(), который печатает "Чирик-чирик!".
#Duck – класс, который наследуется от Bird и Swimmable.

class Flyable:
    def fly(self):
        print("Я умею летать!")

class Swimmable:
    def swim(self):
        print("Я умею плавать!")

class Bird(Flyable):
    def chirp(self):
        print("Чирик-чирик!")

class Duck(Bird, Swimmable):
    pass


donald = Duck()
donald.fly()   # "Я умею летать!"
donald.swim()  # "Я умею плавать!"
donald.chirp() # "Чирик-чирик!"
