# Напишите определение класса File
class File:

    def __init__(self, size_in_bytes=None):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f"{self._size_in_bytes} B"
        elif self._size_in_bytes < 1048576:  # 1024 * 1024 = 1048576 (1 MB)
            size_in_kb = self._size_in_bytes / 1024  # ДЕЛИМ на 1024
            return f"{size_in_kb:.2f} KB"
        elif self._size_in_bytes < 1073741824:
            size_in_mb = self._size_in_bytes / 1048576  # ДЕЛИМ на 1024*1024
            return f"{size_in_mb:.2f} MB"
        else:
            size_in_gb = self._size_in_bytes / 1073741824  # ДЕЛИМ на 1024*1024*1024
            return f"{size_in_gb:.2f} GB"

    @size.setter
    def size(self, size_in_bytes): #имя в сеттере такое же как в геттере
        self._size_in_bytes = size_in_bytes

# Ниже код для проверки методов класса File

file = File(5)
assert file.size == "5 B"
file.size = 1023
assert file.size == "1023 B"
file.size = 1024
assert file.size == "1.00 KB"

file_1 = File(1500000)
assert file_1._size_in_bytes == 1500000
assert file_1.size == "1.43 MB"

file_2 = File(1500)
assert file_2.size == "1.46 KB"


file_3 = File(2789326322)
assert file_3.size == "2.60 GB"
file_3.size = 1073741824
assert file_3.size == "1.00 GB"

print('Good')