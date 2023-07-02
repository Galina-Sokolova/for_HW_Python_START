# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает
# кортеж из трёх элементов: путь, имя файла, расширение файла.
def path_tuple(t: str) -> tuple:
    *a, b = t.split('/')
    file_name, extension = b.split('.')
    path = '/'.join(a)
    return path, file_name, extension


print(path_tuple('C:/Users/79190/PycharmProjects/for_HW_Python_START/HW_5/task_1.py'))
