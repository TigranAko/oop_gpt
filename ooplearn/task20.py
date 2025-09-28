#Инициализация:
#Конструктор принимает количество строк и столбцов (rows, cols).
#Данные хранятся в виде списка списков (self.data).
#Все элементы по умолчанию заполняются нулями.

#Методы:
#__getitem__(self, indices): позволяет получать элемент по индексу [row, col].
#__setitem__(self, indices, value): изменяет элемент по индексу [row, col].
#__str__(): возвращает строковое представление матрицы в удобном формате.

from copy import deepcopy

class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for j in range(rows)] for i in range(cols)]#[[0]*rows]*cols

    def __setitem__(self, item, value):
        self.matrix[item[0]][item[1]] = value

    def __getitem__(self, item):
        return self.matrix[item[0]][item[1]]

    def __str__(self):
        text = "Вывод:\n"
        for i in self.matrix:
            for j in i:
                text = text + str(j) + ' '
            text = text + '\n'
        return text

    def __delitem__(self, item):
        del self.matrix[item[0]][item[1]]

m = Matrix(3, 3) 
print(m)
# Вывод:
# 0 0 0
# 0 0 0
# 0 0 0

m[1, 2] = 5
print(m[1, 2])  # 5

print(m)
# Вывод:
# 0 0 0
# 0 0 5
# 0 0 0
