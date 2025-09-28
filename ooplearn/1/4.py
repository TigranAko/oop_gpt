class Book:
    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year

    def get_summary(self):
        return f"Название: {self._title},\nАвтор: {self._author},\nГод: {self._year}"

book = Book("Грокаем алгоритмы", "А. Бхаргава", 2022)
print(book.get_summary())
