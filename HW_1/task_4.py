#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
#  подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код: from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1
print(f'Угадай целое число от 1 до 1000. У тебя 10 попыток.\n')
while count <= 10:
    n = int(input(f'Попытка {count}, введи число: '))
    if n < num:
        print('Загаданное число больше. Попробуй ещё раз.')
        count += 1
    elif n > num:
        print('Загаданное число меньше. Попробуй ещё раз.')
        count += 1
    else:
        print(f'Молодец! Ты угадал число {num} за {count} попыток!')
    print(f'У тебя осталось {11 - count} попыток.\n')
print(f'К сожалению, тебе не удалось угадать число {num} за 10 попыток')
