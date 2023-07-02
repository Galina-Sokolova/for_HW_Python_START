# Создайте функцию генератор чисел Фибоначчи
def fibonacci_number_generator(num: int):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


print(list(fibonacci_number_generator(15)))
