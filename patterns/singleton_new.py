
class Logger:
    _instance = None


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):
        if not hasattr(self, "logs"):
            self.logs = []


    def log(self, text):
        self.logs.append(text)


    def show_logs(self):
        print(self.logs)


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

logger1.show_logs()  # Должны быть оба сообщения
print(logger1 is logger2)  # True



class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []  # Создаем logs один раз
        return cls._instance

    def log(self, text):
        self.logs.append(text)

    def show_logs(self):
        print(self.logs)


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

logger1.show_logs()  # ['First message', 'Second message']
print(logger1 is logger2)  # True

