# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from pathlib import Path
from random import sample, randint
from typing import Callable


def decor_quadratic_equation(func: Callable):
    def wrapper(*args):
        with open('random_number.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                a, b, c = line
                res = func(float(a), float(b), float(c))
        return res

    return wrapper


def decor_function_results(func):
    file_name = Path(f"{func.__name__}.json")
    json_file = {}

    def wrapper(*args):
        with open(file_name, "w", encoding='utf-8') as fh:
            if args not in json_file:
                json_file[f'{args}'] = func(*args)
                json.dump(json_file, fh, ensure_ascii=False, indent=2)
        return json_file

    return wrapper


@decor_quadratic_equation
@decor_function_results
def find_roots_quadratic_equation(a: float, b: float, c: float):
    if a == 0:
        if b != 0:
            x = -c / b
            return x
        elif c == 0:
            otv = "Уравнение имеет бесконечное множество корней"
            return otv
        else:
            otv = "Уравнение не имеет действительных корней"
            return otv
    discr = b * b - 4 * a * c
    if discr > 0:
        x_1 = (-b + discr ** 0.5) / (2 * a)
        x_2 = (-b - discr ** 0.5) / (2 * a)
        return x_1, x_2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    else:
        otv = "Уравнение не имеет действительных корней"
        return otv


def gen_csv_with_nums():
    min_num = - 10
    max_num = 10
    count_rows = randint(100, 1000)
    rows = []
    for _ in range(count_rows):
        rows.append(sample(range(min_num, max_num), 3))
    with open('random_number.csv', 'w', newline='', encoding='utf-8') as csv_f:
        res = csv.writer(csv_f)
        res.writerows(rows)


if __name__ == "__main__":
    gen_csv_with_nums()
    find_roots_quadratic_equation()
