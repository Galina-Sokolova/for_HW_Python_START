# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
HEX = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
DIS = 16


def convert_num(n: int, b: int) -> str:
    res = []
    while n > 0:
        n, m = divmod(n, b)
        if m in HEX:
            m = HEX[m]
        res.append(str(m))
    return ''.join(res[::-1])


def input_valid_num(n: str) -> int:
    if n.isdigit() and (n1 := int(n)) > 0:
        return n1
    else:
        input_valid_num(input('Введите натуральное число: '))


def compare_res(verif: str, val: int):
    if verif in hex(val):
        print('Конвертация произведена успешно!')
    else:
        print('Error')


def main():
    num = input_valid_num(input('Введите целое число: '))
    conv = convert_num(num, DIS)
    print(conv)
    print(hex(num))
    compare_res(conv, num)


main()
