import threading
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print(finish-start)
        return res
    return wrapper



class Worker(threading.Thread):
    def __init__(self, name, sleep):
        super().__init__()
        self.name = name
        self.sleep = sleep

    @timer
    def run(self):
        print(f"{self.name} начал работу")
        time.sleep(self.sleep)  # Симуляция работы
        print(f"{self.name} завершил работу")

# Запуск нескольких потоков
thread1 = Worker("Поток 1", 2)
thread2 = Worker("Поток 2", 1)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Все потоки завершены")

