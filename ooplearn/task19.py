#Конструктор принимает максимальный размер массива size.
#Метод __getitem__(index) возвращает значение по индексу (если нет сохраненного значения, вернуть 0).
#Метод __setitem__(index, value) устанавливает значение, если оно ненулевое; если value == 0, удаляет ключ из хранения.
#Проверять, что индекс находится в пределах size, иначе выбрасывать IndexError.
#Реализовать __repr__() для наглядного вывода.

class SparseArray:
    def __init__(self, size: int):
        self.size = size
        self.array = {}

    def verify_item(self, index):
        if not 0 <= index < self.size:
            raise IndexError

    def __getitem__(self, item):
        self.verify_item(item)
        if item in self.array:
            return self.array[item]
        else:
            return 0

    def __setitem__(self, item, value):
        self.verify_item(item)
        if value == 0 and item in self.array:
            del self.array[item]
        elif value == 0:
            return
        else:
            self.array[item] = value

    def __delitem__(self, item):
        self.verify_item(item)
        del self.array[item]

    def __str__(self):
        return f"{self.array}"


arr = SparseArray(10)
arr[2] = 5
arr[5] = 3
print(arr[2])  # 5
print(arr[4])  # 0 (так как не устанавливалось)
arr[2] = 0  # удаление значения
print(arr[2])  # 0
print(arr)  # Например, {5: 3}
