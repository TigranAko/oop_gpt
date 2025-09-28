#Класс Subject (Издатель):
#Позволяет подписывать (attach) и отписывать (detach) наблюдателей.
#Оповещает (notify) всех подписчиков при изменении состояния.

#Класс Observer (Наблюдатель) (абстрактный):
#Должен иметь метод update, который будет вызываться при изменении состояния издателя.

#Классы конкретных наблюдателей (EmailObserver, SMSObserver и т. д.):
#Реализуют метод update, который получает уведомление и реагирует соответствующим образом (например, печатает сообщение).

#Создать издателя (например, WeatherStation).
#Подписать на него несколько наблюдателей (EmailObserver, SMSObserver).
#Изменить состояние издателя и убедиться, что все наблюдатели получили уведомление.

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject_state):
        print(f"Изменение состояния {subject_name}:  {subject_state}")


class SMSObserver(Observer):
    def update(self, state):    
        print(f"Отправка SMS: {state}")


class EmailObserver(Observer):
    def update(self, state):
        print(f"Отправка Email: {state}")


class Subject:
    def __init__(self):
        self.observers = set()

    def attach(self, observer: Observer):
        if observer in self.observers:
            print("Пользователь уже подписан")
        else:
            self.observers.add(observer)
            print("Пользователь успешно подписался")


    def detach(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print("Пользователь не сожет отписаться если он не был подписан")

    def notify(self, state):
        for observer in self.observers:
            observer.update(state)

WeatherStation = Subject()
u1 = EmailObserver()
u2 = SMSObserver()
WeatherStation.attach(u1)
WeatherStation.attach(u2)
WeatherStation.notify("+18°C")
