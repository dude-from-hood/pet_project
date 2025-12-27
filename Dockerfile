# 1. Базовый образ с Python (легкая версия Alpine)
FROM python:3.11-alpine

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл зависимостей
COPY common/reqs.txt .

# 4. Устанавливаем Python-зависимости (системные зависимости НЕ НУЖНЫ!)
RUN pip install --no-cache-dir -r reqs.txt

# 5. Копируем весь проект в контейнер
COPY . .

# 6. Команда по умолчанию
CMD ["pytest", "-v", "--tb=short"]