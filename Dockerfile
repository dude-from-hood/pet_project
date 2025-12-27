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

# 6. СОЗДАЕМ config.py С ПРАВИЛЬНЫМ ПУТЕМ
RUN echo "import os" > config.py && \
    echo "ROOT = os.path.dirname(os.path.abspath(__file__))" >> config.py

# 7. Команда по умолчанию
CMD ["pytest", "tests/fake_store/test_mocks.py", "-v", "-s", "--tb=short"]