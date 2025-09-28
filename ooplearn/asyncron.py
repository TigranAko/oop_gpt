import asyncio

class AsyncWorker:
    def __init__(self, name):
        self.name = name

    async def do_work(self):
        print(f"{self.name} начал работу")
        await asyncio.sleep(2)  # Асинхронная пауза
        print(f"{self.name} завершил работу")

async def main():
    worker1 = AsyncWorker("Задача 1")
    worker2 = AsyncWorker("Задача 2")

    await asyncio.gather(worker1.do_work(), worker2.do_work())

asyncio.run(main())

