#Создай базовый класс Message, который будет определять метод send().
#Реализуй три подкласса:
#SMSMessage – отправка SMS (выводит "Отправка SMS на номер ...")
#EmailMessage – отправка Email (выводит "Отправка Email на ...")
#PushNotification – отправка push-уведомления (выводит "Отправка push-уведомления на устройство ...")
#Напиши фабричный метод MessageFactory.create_message(message_type, recipient), который создаёт нужный тип сообщения.

class SMSMessage:
    def __init__(self, sendto):
        self.sendto = sendto

    def send(self, text=None):
        if text:
            print(f"Отправка SMS на номер {self.sendto}: {text}")
        else:
            print(f"Отправка SMS на номер {self.sendto}")


class EmailMessage:
    def __init__(self, sendto):
        self.sendto = sendto

    def send(self, text=None):
        if text:
            print(f"Отправка Email на номер {self.sendto}: {text}")
        else:
            print(f"Отправка Email на номер {self.sendto}")



class PushNotification:
    def __init__(self, sendto):
        self.sendto = sendto

    def send(self, text=None):
        if text:
            print(f"Отправка PushNotification на номер {self.sendto}: {text}")
        else:
            print(f"Отправка PushNotification на номер {self.sendto}")




class MessageFactory:
    @staticmethod
    def create_message(message_type, sendto):
        match message_type:
            case "sms":
                return SMSMessage(sendto)
            case "email":
                return EmailMessage(sendto)
            case "push":
                return PushNotification(sendto)



msg1 = MessageFactory.create_message("sms", "+123456789")

msg1.send()  # Отправка SMS на номер +123456789  

msg2 = MessageFactory.create_message("email", "test@example.com")
msg2.send()  # Отправка Email на test@example.com  

msg3 = MessageFactory.create_message("push", "device_001")
msg3.send()  # Отправка push-уведомления на устройство device_001  
#Добавь возможность задавать текст сообщения в методе send(), например:

msg1.send("Привет!")  # Отправка SMS на номер +123456789: Привет!
