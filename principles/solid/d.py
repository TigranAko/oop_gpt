#bad
class EmailNotifier:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Order:
    def __init__(self):
        self.notifier = EmailNotifier()  # Жёсткая зависимость от EmailNotifier

    def complete_order(self):
        print("Order completed!")
        self.notifier.send_email("Your order is complete!")  # Прямая зависимость


from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class EmailNotifier:
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotifier:
    def send(self, message):
        print(f"Sending sms: {message}")

class Order:
    def __init__(self, notifier: Notifier):
        self.notifier = Notifier()

    def complete_order(self):
        print("Order completed!")
        self.notifier.send("Your order is complete!")  # Прямая зависимость

# best

from abc import ABC, abstractmethod

# Абстракция для уведомлений
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Реализация для Email
class EmailNotifier(Notifier):  # Наследуем Notifier
    def send(self, message):
        print(f"Sending email: {message}")

# Реализация для SMS
class SMSNotifier(Notifier):  # Наследуем Notifier
    def send(self, message):
        print(f"Sending SMS: {message}")

# Order теперь зависит от абстракции
class Order:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier  # Передаём готовый объект

    def complete_order(self):
        print("Order completed!")
        self.notifier.send("Your order is complete!")  # Вызываем метод через абстракцию

# Тестируем
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

order1 = Order(email_notifier)
order1.complete_order()
# Output:
# Order completed!
# Sending email: Your order is complete!

order2 = Order(sms_notifier)
order2.complete_order()
# Output:
# Order completed!
# Sending SMS: Your order is complete!

