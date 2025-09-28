
#Реализуйте класс ComputerFacade, который инкапсулирует работу всех трёх компонентов.
#Добавьте в него метод start_computer(), в котором:
#Процессор "замораживается"
#С диска читаются данные
#В память загружаются данные
#Процессор переходит к нужному адресу
#Процессор начинает выполнение
#Клиент должен вызывать только start_computer(), ничего не зная про CPU, память и диск.

class CPU:
    def freeze(self):
        print("Freezing processor")

    def jump(self, position):
        print(f"Jumping to {position}")

    def execute(self):
        print("Executing instructions")


class Memory:
    def load(self, position, data):
        print(f"Loading data '{data}' to position {position}")


class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from address {lba}")
        return "OS boot data"

class ComputerFacade:
    def __init__(self, cpu: CPU, memory: Memory, hard_drive: HardDrive):
        self.cpu = cpu
        self.memory = memory
        self.hard_drive = hard_drive 

    def start_computer(self):
        position = 1000
        self.cpu.freeze()
        data = self.hard_drive.read(100, 512)
        self.memory.load(position, data)
        self.cpu.jump(position)
        self.cpu.execute()

cpu = CPU()
memory = Memory()
hard_drive = HardDrive()

computer = ComputerFacade(cpu, memory, hard_drive)
computer.start_computer()

#Freezing processor
#Reading 512 bytes from address 100
#Loading data 'OS boot data' to position 1000
#Jumping to 1000
#Executing instructions
