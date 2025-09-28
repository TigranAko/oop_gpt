
class Projector:
    def turn_on(self):
        print("Включение", self.__class__.__name__)
    def turn_off(self):
        print("Отключение", self.__class__.__name__)


class Amplifier:
    def turn_on(self):
        print("Включение", self.__class__.__name__)
    def turn_off(self):
        print("Отключение", self.__class__.__name__)
    def set_volume(self):
        print("Изменение громкости")

class Service:
    def connect(self):
        print("Подключение")
    def play_film(self, title):
        print("Включение фильма",  title)

class HomeTheaterFacade:
    def __init__(self, projector, amplifier, service):
        self.projector = projector
        self.amplifier = amplifier
        self.service = service

    def watch_movie(self, title):
        self.projector.turn_on()
        self.amplifier.turn_on()
        self.service.connect()
        self.service.play_film(title)

    def end_movie(self):
        self.projector.turn_off()
        self.amplifier.turn_off()
    
projector = Projector()
amplifier = Amplifier()
service = Service()

facade = HomeTheaterFacade(projector, amplifier, service)
facade.watch_movie("Interstellar")
facade.end_movie()

