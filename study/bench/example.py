import time


def bench(func, *args, repeats=1000, **kwargs):
    """Замеряет среднее время выполнения функции"""
    total_time = 0
    for _ in range(repeats):
        start = time.perf_counter()  # Точный таймер
        func(*args, **kwargs)
        total_time += time.perf_counter() - start
    return total_time / repeats  # Среднее время


# Пример использования
def sum_function():
    return sum(range(10000))

avg_time = bench(sum_function, repeats=100000)
print(f"Среднее время: {avg_time:.6f} секунд")
