#Задача: Обработка заказов в интернет-магазине
#Тебе нужно создать класс OrderProcessor, который обрабатывает заказы в интернет-магазине. У каждого заказа есть:
#номер заказа
#название товара
#время обработки (симуляция задержки в 2 секунды)

from abc import ABC
from threading import Thread
from multiprocessing import Process
from time import sleep
import asyncio

class Order(ABC):
#    def __init__(self, number, title, timer=2):
#        self.number = number
#        self.title = title
    def __init__(self, orders: list[int, str], timer=2):
        self.orders = orders
        self.timer = timer
        self.process: list[(Thread, Process)] = []

    def process_order(self, number, title):
        print(f"Заказ {number} ({title}) обрабатывается")
        sleep(self.timer)
        print(f"Обработка заказа {number} завершается")

    def start(self):
#        print("Запускается обработка")
        for process in self.process:
            process.start()

    def wait(self):
        for process in self.process:
#            print("Ожидается завершение заказа")
            process.join()
        print("Все заказы завершены\n")


class OrderProcessor(Order):
    def __init__(self, orders, timer=2):
        super().__init__(orders, timer)
        self.process = [Process(target = self.process_order, args=(number, title)) for number, title in orders]


orders = [
    (1, "Телефон"),
    (2, "Ноутбук"),
    (3, "Книга")
]
 
processor = OrderProcessor(orders)
processor.start()
processor.wait()

class OrderThread(Order):
    def __init__(self, orders, timer=2):
        super().__init__(orders, timer) 
        self.process = [Thread(target = self.process_order
, args=(number, title)) for number, title in orders]
 
processor = OrderThread(orders)
processor.start()
processor.wait()


class AsyncOrderProcessor:
    def __init__(self, orders):
        self.orders = orders


    async def process_order(self, number, title):
        print(f"Заказ {number} ({title}) обрабатывается")
        await asyncio.sleep(2)
        print(f"Обработка заказа {number} завершается")


    async def start(self):
        for number, title in self.orders:
            await self.process_order(number, title)


async def main():
    orders = [
        (1, "Телефон"),
        (2, "Ноутбук"),
        (3, "Книга")
    ]
    processor = AsyncOrderProcessor(orders)
    await processor.start()

asyncio.run(main())



#Требования:
#Реализуй 3 версии класса OrderProcessor:
#С потоками (threading) – каждый заказ обрабатывается в отдельном потоке.
#С процессами (multiprocessing) – каждый заказ обрабатывается в отдельном процессе.
#С asyncio – заказы обрабатываются асинхронно.
#У каждого варианта должны быть методы:
#process_order() – имитация обработки заказа (выводит сообщение и ждет 2 секунды).
#start() – запускает обработку.
#wait() (для threading и multiprocessing) – ожидает завершения всех заказов.

#Пример работы (threading и multiprocessing):

#Вывод (параллельный, порядок может отличаться):

#Заказ 1 (Телефон) в обработке...
#Заказ 2 (Ноутбук) в обработке...
#Заказ 3 (Книга) в обработке...
#Заказ 1 обработан!
#Заказ 2 обработан!
#Заказ 3 обработан!

#Пример работы (asyncio):
#Вывод (асинхронный, порядок может отличаться):

#Заказ 1 (Телефон) в обработке...
#Заказ 2 (Ноутбук) в обработке...
#Заказ 3 (Книга) в обработке...
#Заказ 1 обработан!
#Заказ 2 обработан!
#Заказ 3 обработан!

#Цель
#Ты должен написать 3 варианта OrderProcessor и протестировать их.
