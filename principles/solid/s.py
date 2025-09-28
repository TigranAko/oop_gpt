class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User {user} added")
        self.send_email(user, "Welcome!")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user} removed")
            self.send_email(user, "Goodbye!")

    def send_email(self, user, message):
        print(f"Sending email to {user}: {message}")
# Its bad.^

# good
class UserDatabase:
    """Класс для управления пользователями"""
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User {user} added")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"User {user} removed")


class SendEmail:
    """Класс для отправки email-уведомлений"""
    @staticmethod
    def send_email(user, message):
        print(f"Sending email to {user}: {message}")


class UserManager:
    """Класс для работы с пользователями, координирует работу других классов"""
    def __init__(self, database, email_service):
        self.database = database
        self.email_service = email_service

    def add_user(self, user):
        self.database.add_user(user)
        self.email_service.send_email(user, "Welcome!")

    def remove_user(self, user):
        self.database.remove_user(user)
        self.email_service.send_email(user, "Goodbye!")


# Использование
db = UserDatabase()
email_service = SendEmail()
manager = UserManager(db, email_service)

manager.add_user("Alice")
manager.remove_user("Alice")

