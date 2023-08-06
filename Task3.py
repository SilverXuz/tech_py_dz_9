# ------------------------------------------- 1 -----------------------------
"""
Напишите следующие функции:
    ○ Нахождение корней квадратного уравнения
    ○ Генерация csv файла с тремя случайными числами в каждой строке.
      100-1000 строк.
    ○ Декоратор, запускающий функцию нахождения корней квадратного
      уравнения с каждой тройкой чисел из csv файла.
    ○ Декоратор, сохраняющий переданные параметры и результаты работы
      функции в json файл.
"""

# Не решил. Взял ваше решение, разбор посмотрел


import csv
import json
import os.path
from functools import wraps
from random import randint


def calc_roots_dec(func):
    @wraps(func)
    def wrapper():
        file_name = f"{func.__name__}.csv"
        gen_nums_to_csv(file_name)
        with open(file_name, newline='') as f_read:
            f_read.readline()
            for line in f_read:
                func(*map(int, line.split(",")))

    return wrapper


def save_to_json_dec(func):
    @wraps(func)
    def wrapper(*args):
        all_data = {}
        file_name = f"{func.__name__}.json"
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f_read:
                all_data = json.load(f_read)

        with open(file_name, "w", encoding="utf-8") as f_write:
            all_data[str(args)] = func(*args)
            json.dump(all_data, f_write, indent=2, ensure_ascii=False)

    return wrapper


def gen_nums_to_csv(file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as f_write:
        csv_write = csv.writer(f_write, dialect='excel')
        csv_write.writerow(["a", "b", "c"])
        csv_write.writerows([[randint(-100, 100), randint(-100, 100), randint(-100, 100)]
                             for _ in range(randint(100, 1000))])


@calc_roots_dec
@save_to_json_dec
def find_roots(a=1, b=1, c=1):
    if a == 0:
        return 'Коэффициент (a) = 0'
    d = b ** 2 - 4 * a * c
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    if d > 0:
        result = f'2 корня: {x_1 = } и {x_2 = }'
    elif d == 0:
        result = f'1 корень: {x_1 = }'
    else:
        result = f'Комплексные корни: {x_1 = } и {x_2 = }'

    return result


if __name__ == "__main__":
    find_roots()
