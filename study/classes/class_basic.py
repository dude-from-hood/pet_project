from dataclasses import dataclass, field
import datetime


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)


dog = Dog('gilbert', 12)
print(dog)


#+-----------Задачи---------------
#1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self._year = year

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.year})"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        """
        Определяет поведение оператора '<' (меньше чем).
        """
        if isinstance(other, Book):
            return self.year < other.year
        else:
            # Можно поднять ошибку или вернуть NotImplemented
            return NotImplemented

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value > datetime.datetime.now().year:
            raise ValueError("Год не может быть больше текущего!")
        else:
            self._year = value

    def get_info(self):
        return f"{self.title} - {self.author} ({self.year})"

    @staticmethod
    def is_valid_title(title):
        return len(title.strip()) > 1


book1 = Book("mkm", 'Bob', 2015)
book2 = Book("zkm", 'Tom', 1915)
print(book2.year)
book2.year = 2020
print(book2.year)
print(Book.is_valid_title(' aa'))


#2 - наследование
class Ebook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def get_info(self):
        return f"{self.title} - {self.author} ({self.year}) [{self.file_size} МБ]"


ebook_obj = Ebook('ebook_title', "Donnie", 2022, 5)
print(ebook_obj.get_info())


#3 - dataclass
@dataclass
class BookData:
    title: str
    author: str = field(init=True, compare=False)
    year: int
    price: float = 0.0


book_data1 = BookData("Python", "Author A", 2020)
book_data2 = BookData("Python", "Author B", 2020)

print(book_data1 == book_data2)  # True (автор игнорируется в сравнении)
