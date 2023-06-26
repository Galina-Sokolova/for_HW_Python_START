# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль
# fractions.
import fractions
import math


def input_valid_num(n: str) -> int:
    if n.isdigit():
        return int(n)
    else:
        input_valid_num(input('Введите число: '))


def reduce_fraction(n, d):
    if n == d:
        return 1
    if n == 0 or d == 0:
        return 0
    nod = math.gcd(n, d)
    n = n / nod
    d = d / nod
    return f'{int(n)}/{int(d)}'


def sum_fractions(n1: int, d1: int, n2: int, d2: int):
    d = d1 * d2
    n = n1 * d2 + n2 * d1
    res = reduce_fraction(n, d)
    return res


def mult_fractions(n1: int, d1: int, n2: int, d2: int):
    d = d1 * d2
    n = n1 * n2
    res = reduce_fraction(n, d)
    return res


numerator_1 = input_valid_num((input('Введите числитель первой дроби: ')))
denominator_1 = input_valid_num(input('Введите знаменатель первой дроби: '))
numerator_2 = input_valid_num((input('Введите числитель второй дроби: ')))
denominator_2 = input_valid_num(input('Введите знаменатель второй дроби: '))
f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)
res_sum = sum_fractions(numerator_1, denominator_1, numerator_2, denominator_2)
res_mult = mult_fractions(numerator_1, denominator_1, numerator_2, denominator_2)
print(f'{numerator_1}/{denominator_1} + {numerator_2}/{denominator_2} = {res_sum}')
print(f1 + f2)
print(f'{numerator_1}/{denominator_1} * {numerator_2}/{denominator_2} = {res_mult}')
print(f1 * f2)
