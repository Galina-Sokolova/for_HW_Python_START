# Вывести в консоль таблицу умножения

START = 2
FIRST_FACTOR = 9
SECOND_FACTOR = 11
STEP = 4

print(' ' * 25 + 'ТАБЛИЦА УМНОЖЕНИЯ')

for series in range(START, FIRST_FACTOR, STEP):
    for i in range(START, SECOND_FACTOR):
        for j in range(series, series + STEP):
            print(f'{j}  x {i:>2}  =  {i * j:2}', end=' '*5)
        print()
    print()
