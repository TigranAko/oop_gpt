import multiprocessing
import time

class Worker(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} начал работу")
        time.sleep(2)
        print(f"{self.name} завершил работу")

process1 = Worker("Процесс 1")
process2 = Worker("Процесс 2")

process1.start()
process2.start()

process1.join()
process2.join()
print("Все процессы завершены")

