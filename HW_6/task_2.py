# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите
# 4 успешных расстановки.
from task_1_2 import get_random_pos, check_queens_disposition

count_rank = 4

while count_rank:
    pos = get_random_pos()
    if check_queens_disposition(pos):
        print(pos)
        count_rank -= 1