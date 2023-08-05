# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет
# есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа. Если пользователь
# присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень доступа
# и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа,
# вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json

from HW_13.Exceptions import AccessError, LevelError
from HW_13.user_class import User


class Project:
    def __init__(self, users_lst=None):
        if users_lst is None:
            self.users_lst = []
        self.users_lst = users_lst
        self.admin = None

    @classmethod
    def get_users_list(cls):
        with open('users.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return cls(temp)

    def login(self, u_id, name):
        user = User(u_id, name)
        if user not in self.users_lst:
            raise AccessError(name)
        for u in self.users_lst:
            if user == u:
                self.admin = u
                break

    def add_user(self, u_id, name, level):
        if level < self.admin.level:
            raise LevelError(self.admin.name)
        user = User(u_id, name, level)
        self.users_lst.append(user)

    def del_user(self, u_id, name, level):
        if level < self.admin.level:
            raise LevelError(self.admin.name)
        user = User(u_id, name, level)
        try:
            self.users_lst.remove(user)
        except ValueError:
            print('Пользователя нет в списке')

    def __repr__(self):
        return f'Project({self.users_lst}, admin = {self.admin})'

    def __exit__(self, exc_type, exc_value, traceback):
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(self.users_lst, f)


g = Project.get_users_list()
print(g)
g.login('34', 'Alex')
print(g)
g.add_user('232', 'Olga', 4)
print(g)
g.add_user('349', 'Sonja', 1)
print(g)
g.del_user('337', 'Max', 5)
