class DatabaseConnection:
    def __enter__(self):
        print("Подключение к базе данных")
        return self #DataBase

    def __exit__(self, exc_type, exc_value, traceback):
        print("Отключение от базы данных")
        del self # close DataBase 

with DatabaseConnection() as db:
    print("Запрос к базе данных")

#__enter__ должен выводить "Подключение к базе данных" и возвращать объект соединения (можно просто self).
#__exit__ должен выводить "Отключение от базы данных" и закрывать соединение.
#Внутри блока with можно выполнять условные операции (например, print("Запрос к базе данных")).


#Подключение к базе данных
#Запрос к базе данных
#Отключение от базы данных

class FileHandler:
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Возникла ошибка: {exc_type} - {exc_value}")
        if hasattr(self, "file"):
            self.file.close()
        return True # Ошибка обработана


with FileHandler('example.txt', 'w') as file:
    file.write("Hello, world!")
    # raise ValueError("Произошла ошибка!")  # Для теста ошибки

with FileHandler('non_existent_file.txt', 'r') as file:
    content = file.read()  # Ожидается ошибка, так как файл не существует

