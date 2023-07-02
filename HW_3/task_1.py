# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
friends = {'Alex': ('палатка', 'лодка', 'спички', 'нож', 'котелок', 'удочки', 'эл.плитка', 'соль'), \
           'Max': ('матрас', 'топор', 'соль', 'спички', 'нож', 'продукты', 'удочки', 'вода'), \
           'Elen': ('раптор', 'солнцезащитный крем', 'мяч', 'бадминтон', 'матрас', 'соль', 'удочки', 'сковорода')
           }

all_things_friends = set()
for i in friends:
    all_things_friends = all_things_friends.union(set(friends[i]))
print(f'Все три друга взяли: {all_things_friends}')
print('*' * 25)

for i in friends:
    unique_things = set(friends[i])
    for j in friends:
        if i != j:
            unique_things = unique_things.difference(friends[j])
    print(f'Только {i} взял {unique_things}')
print('*' * 25)

for i in friends:
    temp = set()
    for j in friends:
        if i != j:
            if len(temp) == 0:
                temp = temp.union(set(friends[j]))
            else:
                temp.intersection_update(set(friends[j]))
    print(f'Только у {i} нет: {temp.difference(set(friends[i]))}')
