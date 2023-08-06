"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
# Не решил. Взял ваше решение, разбор посмотрел

from typing import Callable

def repeat_runs(count: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper
    return decorator

@repeat_runs(count=33)
def print_hello():
    print("Hello, world!")
