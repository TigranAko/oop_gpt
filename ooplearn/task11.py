#1. Композиция (жесткая связь)
#Создай класс Computer, который состоит из:
#
#Processor (процессор)
#RAM (оперативная память)
#Когда создается Computer, он сам создает внутри себя процессор и оперативную память.

#✅ Реализуй:

#Computer должен иметь метод specs(), который выводит характеристики компьютера.
#Processor и RAM должны иметь свои параметры (например, мощность процессора и объем памяти).
class Processor:
    def __init__(self, power):
        self.power = power

class RAM:
    def __init__(self, memory: float):
        self.memory = memory

class Computer:
    def __init__(self, memory):
        self.processor = Processor(5000)
        self.ram = RAM(memory)

    def specs(self):
        print(f"Мощность: {self.processor.power}, Объем памяти: {self.ram.memory}")

c = Computer(32)
c.specs()

#2. Агрегирование (гибкая связь)
#Создай класс Library, который содержит книги (но не владеет ими полностью!).

#Класс Book создается отдельно.
#Класс Library просто хранит ссылки на существующие книги.
#✅ Реализуй:

#Метод add_book(book), который добавляет книгу в библиотеку.
#Метод show_books(), который выводит список книг в библиотеке.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.library = list()

    def add_book(self, book: Book):
        self.library.append(book)

    def show_books(self):
        print("Книги в библиотеке:")
        for book in self.library:
            print(f"- {book.title} ({book.author})")


book1 = Book("1984", "Джордж Оруэлл")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.show_books()

#Ожидаемый результат:
#Книги в библиотеке:
#- 1984 (Джордж Оруэлл)
#- Мастер и Маргарита (Михаил Булгаков)
