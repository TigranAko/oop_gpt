class UserAccount:
    def __init__(self, username, email, notification_type):
        self.username = username
        self.email = email
        self.notification_type = notification_type
        self.notification_preferences = []

    def set_notification_preferences(self):
        # Добавляем дополнительные опции, которые могут не понадобиться
        if self.notification_type == "email":
            self.notification_preferences.append("send_email")
        elif self.notification_type == "sms":
            self.notification_preferences.append("send_sms")
        elif self.notification_type == "push":
            self.notification_preferences.append("send_push_notification")
        else:
            self.notification_preferences.append("default")


class UserAccount:
    def __init__(self, username, email, notification_type):
        self.username = username
        self.email = email
        self.notification_preferences = []

    def set_notification_preferences(self):
        # Добавляем дополнительные опции, которые могут не понадобиться
        self.notification_preferences.append("send_email")

