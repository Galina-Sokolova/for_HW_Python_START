#2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем
# списке не должно быть дубликатов.
list = [1, 2, 4, 2, 3, 1, 5, 6, 6, 7, 7, 8, 3, 2, 1]
set_list = set(list)
new_list = []
for i in set_list:
    new_list.append(i)
print(new_list)
