def singleton(cls):
    _instance = {}
    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return wrapper


@singleton
class Logger:
    def __init__(self):
        self.logs = []

    def log(self, text):
        self.logs.append(text)

    def show_logs(self):
        print(self.logs)

logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

logger1.show_logs()  
# Должно вывести: ["First message", "Second message"]

print(logger1 is logger2)  # True

