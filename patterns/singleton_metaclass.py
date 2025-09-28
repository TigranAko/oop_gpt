class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__()
        return cls._instance[cls]

class DatabaseConnection(metaclass=Singleton):
    def __init__(self, server="localhost"):
        self.server = server

    def connect(self):
        print(f"Connecting to {self.server}")


db1 = DatabaseConnection("localhost")
db2 = DatabaseConnection("127.0.0.1")

print(db1 is db2)  # Должно быть True

db1.connect()  # "Connecting to localhost"
db2.connect()  # "Connecting to localhost" (не "127.0.0.1"!)

