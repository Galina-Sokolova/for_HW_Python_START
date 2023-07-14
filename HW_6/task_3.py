# Выведите все успешные варианты расстановок


from task_1_2 import generate_disposition as gd

NUMBER_QUEENS = 8
current_pos = [0 for data in range(NUMBER_QUEENS)]
combinations = gd(0, NUMBER_QUEENS, current_pos)

print(*combinations, sep='\n')
print(f'{len(combinations)} вариантов найдено: ')
