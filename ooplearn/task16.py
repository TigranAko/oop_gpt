#Напиши класс RangeGenerator, который работает как встроенная range(), но реализован с помощью генераторов.

#Требования:
#Конструктор принимает start, end, step.
#Метод __iter__() должен использовать yield.
#При каждом вызове генератор должен возвращать следующее число последовательности.
#Если step < 0, последовательность должна уменьшаться.
#Если step == 0, выбрасывай ValueError("Шаг не может быть 0!").

class RangeGenerator:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        if step == 0:
            raise ValueError("Шаг не может быть 0!")
        self.step = step
        self.value = self.start


    def __iter__(self):
        value = self.start
        while self.end<self.start and value > self.end or self.end>self.start and value<self.end:
            yield value 
            value += self.step

        # ИЛИ
        #for i in range(self.start, self.end, self.step):
        #    yield i


gen = RangeGenerator(1, 10, 2)
for num in gen:
    print(num)  
# Вывод: 1, 3, 5, 7, 9

gen = RangeGenerator(10, 0, -2)
for num in gen:
    print(num)  
# Вывод: 10, 8, 6, 4, 2

try:
    gen = RangeGenerator(1, 5, 0)  
except ValueError as e:
    print(e)
# ValueError: Шаг не может быть 0!
