# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть
# один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
from itertools import combinations

WEIGHT_LIMIT = 12
things = {"палатка": 6, "матрас": 2, "котелок": 0.5, "нож": 0.2, "спички": 0.05, "консервы": 0.5, "крупа": 0.5,
          "хлеб": 0.5, "вода": 1, "топор": 1.5, "шашлык": 2, "картофель": 2.0, "удочки": 1.5, "прикормка": 1}
result = []

for i in range(len(things)):
    items_combinations = combinations(things, i)
    for combination in items_combinations:
        temp_dict = things.copy()
        weight = 0
        for item in combination:
            weight += things[item]
            temp_dict.pop(item)
        if weight <= WEIGHT_LIMIT:
            min_weight_things = min(temp_dict.items(), key=lambda x: x[1])
            if weight + min_weight_things[1] <= WEIGHT_LIMIT:
                continue
            else:
                result.append(list(combination) + [weight])
for data in result:
    print(data)
