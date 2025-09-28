#Создай класс PositiveNumber, который будет дескриптором, проверяющим, что значение неотрицательное.
#Используй его в классе BankAccount для хранения баланса.
#
#Требования:
#PositiveNumber должен проверять, что число >= 0.
#В BankAccount атрибут balance должен использовать этот дескриптор.
#При попытке присвоить отрицательное значение должно выбрасываться исключение.

class PositiveNumber:
    def __init__(self, number: float):
        if self.verify(number): # если нет ошибок
            self.number = number

    def __get__(self):
        return self.number

    def __set__(self, new_number):
        if self.verify(new_number):
            raise ValueError("Число должно быть положительным")
        self.number = new_number
    
    @classmethod
    def verify(cls, number):
        if not isinstance(number, (int, float)):
            raise TypeError("number должно быть типа float or int")
        elif number < 0:
            raise ValueError("Число должно быть положительным")
        return True
        



class BankAccount:
    def __init__(self, balance):
        self.balance = PositiveNumber(balance)

    def __str__(self):
        return f"{self.balance.number}"

a = BankAccount(5200.50)
print(a)
