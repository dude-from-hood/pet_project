import psycopg2
from psycopg2._psycopg import connection
import os
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

# Загружаем переменные из .env
load_dotenv()

current_connections: List[connection] = []  # активные подключения к БД


# --- Структура данных ---
class QueryResult:
    """
    Результат SELECT-запроса к БД
    """
    def __init__(self):
        self.rowcount: int = 0
        self.first_row: Dict[str, Any] = {}
        self.rows: List[Dict[str, Any]] = []


# --- Контекстный менеджер для PostgreSQL ---
class Postgres:
    """
    Контекстный менеджер для работы с PostgreSQL через psycopg2.
    Использование:
        with Postgres(dbname='mydb') as db:
            result = db.select("SELECT * FROM users")
    """
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        database_name: Optional[str] = None
    ):
        # Берём значения из .env, если не переданы
        self.host = host or os.getenv('DB_HOST')
        self.port = port or os.getenv('DB_PORT')
        self.user = user or os.getenv('DB_USER')
        self.password = password or os.getenv('DB_PASSWORD')
        self.database_name = database_name or os.getenv('DB_NAME')

        self.conn: Optional[connection] = None

    def __enter__(self):
        self.conn = find_conn(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database_name=self.database_name
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # В данном случае мы не закрываем соединение, потому что оно может использоваться в пуле
        # Но можно добавить опцию, например auto_close=True, чтобы при желании закрывать
        if exc_type:
            print(f"Ошибка в контексте Postgres: {exc_value}")
        # Пока не закрываем, т.к. find_conn управляет общими соединениями
        return False  # Не подавляем исключения

    def select(self, text_query: str) -> QueryResult:
        """Выполняет SELECT-запрос и возвращает QueryResult"""
        if not self.conn:
            raise RuntimeError("Соединение не установлено. Используйте контекстный менеджер 'with'.")

        res = QueryResult()

        with self.conn.cursor() as cursor:
            cursor.execute(text_query)
            clmn_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            res.rowcount = len(rows)

            if rows:
                res.first_row = dict(zip(clmn_names, rows[0]))
                res.rows = [dict(zip(clmn_names, row)) for row in rows]

        return res

    def crud(self, text_query: str) -> int:
        """Выполняет INSERT/UPDATE/DELETE и возвращает количество затронутых строк"""
        if not self.conn:
            raise RuntimeError("Соединение не установлено. Используйте контекстный менеджер 'with'.")

        with self.conn.cursor() as cursor:
            cursor.execute(text_query)
            affected = cursor.rowcount
            self.conn.commit()
            return affected


# --- Функции управления подключениями ---
def new_database_connection(
    host: str,
    port: str,
    user: str,
    password: str,
    database_name: str
) -> connection:
    """Создаёт новое подключение к БД"""
    return psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database_name
    )


def find_conn(
    host: str,
    port: str,
    user: str,
    password: str,
    database_name: str
) -> connection:
    """Ищет активное подключение или создаёт новое"""
    for conn in current_connections:
        if conn.info.dbname == database_name:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return conn
            except psycopg2.OperationalError:
                current_connections.remove(conn)
                break  # найдено, но битое — продолжим создание нового

    # Создаём новое подключение
    conn = new_database_connection(
        host=host,
        port=port,
        user=user,
        password=password,
        database_name=database_name
    )
    current_connections.append(conn)
    return conn


# --- Тестирование ---
if __name__ == '__main__':
    import pprint

    with Postgres() as db:
        result = db.select("SELECT * FROM rnc_database LIMIT 5")

        pprint.pp(result.first_row)
        print(f"Количество записей: {result.rowcount}")

        # Пример CRUD (на ваше усмотрение)
        # rows_affected = db.crud("UPDATE ...")
        # print(f"Обновлено строк: {rows_affected}")