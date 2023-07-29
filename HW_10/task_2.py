# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
class NumberType:

    def __init__(self):
        self.num = int(input('Введите число от 1 до 100 000: '))

    def nums_is_type(self):
        while True:
            if 1 <= self.num <= 100000:
                for i in range(2, int(self.num ** 0.5) + 1):
                    if self.num % i == 0:
                        result = f'Число {self.num} является составным'
                        break
                else:
                    result = f'Число {self.num} является простым'
                break
        return result


if __name__ == "__main__":
    new_num = NumberType()
    print(new_num.nums_is_type())
