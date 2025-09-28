#Реализуй систему управления папками и файлами с помощью паттерна Компоновщик.

#Папка (Folder) может содержать файлы (File) и другие папки.

#Файл (File) имеет имя и размер (в KB).

#Метод show(indent=0) должен выводить структуру папок и файлов с отступами.

#Метод size() у Folder должен возвращать суммарный размер всех вложенных файлов.
from abc import ABC, abstractmethod
from typing import List

class FolderOrFile(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass
    
    @abstractmethod
    def size(self):
        pass

class Folder(FolderOrFile):
    def __init__(self, name: str):
        self.name = name
        self.children: List[FolderOrFile] = []

    def show(self, indent=0):
        print(f"{indent*'\t'} 📂 {self.name}")
        for child in self.children:
            child.show(indent+1)

    def add(self, item: FolderOrFile):
        self.children.append(item)

    def size(self):
        return sum(map(lambda item: item.size(), self.children))
#        sum({item.size() for item in self.children})

class File(FolderOrFile):
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size

    def show(self, indent=0):
        print(f"{indent*'\t'} 📄 {self.name} ({self.size()} KB)")

    def size(self):
        return self._size


root = Folder("Root")
docs = Folder("Documents")
pics = Folder("Pictures")

file1 = File("resume.pdf", 120)
file2 = File("photo.jpg", 2000)
file3 = File("notes.txt", 45)

docs.add(file1)
pics.add(file2)
root.add(docs)
root.add(pics)
root.add(file3)

root.show()
print(f"Total size: {root.size()} KB")
# Root
#    📂 Documents
#         resume.pdf (120 KB)
#    📂 Pictures
#        📄 photo.jpg (2000 KB)
#    📄 notes.txt (45 KB)
#Total size: 2165 KB








