class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
        print(f"Инициализирован FileManager для файла '{filename}'")

    def __enter__(self):
        # Вызывается при входе в блок with
        print(f"Открываем файл '{self.filename}' в режиме '{self.mode}'")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        # Возвращаем сам файловый объект для работы в блоке with
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Вызывается при выходе из блока with
        print(f"Закрываем файл '{self.filename}'")

        if self.file:
            self.file.close()

        # Обработка ошибок
        if exc_type is not None:
            print(f"Произошла ошибка: {exc_type}: {exc_val}")
            # Если вернем True - исключение будет подавлено
            # Если False - исключение продолжится
            return False

        print("Операции с файлом завершены успешно")
        return True


if __name__ == '__main__':
    print("=== Сценарий 1: Успешная запись в файл ===")
    with FileManager('test.txt', 'w') as f:
        f.write("Первая строка\n")
        f.write("Вторая строка\n")
        print("Данные записаны в файл")

    print("Программа продолжает работу...")

    print("\n=== Сценарий 2: Чтение из файла ===")
    with FileManager('test.txt', 'r') as f:
        content = f.read()
        print("Содержимое файла:")
        print(content)