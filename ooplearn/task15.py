#Класс EvenNumbers должен принимать два числа:

#start (начальное значение)
#end (конечное значение)
#Должен поддерживать итерацию с помощью for и next().

#Метод __iter__() должен возвращать сам объект.

#Метод __next__() должен:

#Выдавать следующее чётное число.
#Если чётных чисел больше нет — вызывать StopIteration.
#Пример работы:

class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        if self.start % 2 == 1:
            self.start += 1
        value = self.start
        self.start += 2
        return value

    def __len__(self):
        return round((self.end - self.start)/2)


evens = EvenNumbers(3, 10)

print(next(evens))  # 4
print(next(evens))  # 6
print(next(evens))  # 8
print(next(evens))  # 10
try:
    print(next(evens))  # Ошибка StopIteration
except StopIteration:
    print("StopIteration Error")

for num in EvenNumbers(7, 15):
    print(num)  

# Выведет: 8, 10, 12, 14
#Дополнительное задание (если хочешь усложнить):
#Сделай так, чтобы EvenNumbers поддерживал len(), возвращая количество чётных чисел в диапазоне.

evens = EvenNumbers(3, 10)
print(len(evens))  # 4 (четные числа: 4, 6, 8, 10)
