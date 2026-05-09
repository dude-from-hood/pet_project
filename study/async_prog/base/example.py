
import asyncio
import time

async def fetch_data(seconds):
    print(f"Начинаем запрос на {seconds} секунды")
    await asyncio.sleep(seconds)
    print(f"Запрос на {seconds} секунды прошёл успешно")

async def main():
    start = time.perf_counter()

    # Пример 1: Ручное создание задач через create_task()
    # task1 = asyncio.create_task(fetch_data(2))
    # task2 = asyncio.create_task(fetch_data(4))
    # task3 = asyncio.create_task(fetch_data(3))

    # await task1
    # await task2
    # await task3

    # Пример 2: Использование asyncio.gather()
    await asyncio.gather(fetch_data(2), fetch_data(4), fetch_data(3))

    print(f"Время исполнения: {time.perf_counter() - start}")

asyncio.run(main())

