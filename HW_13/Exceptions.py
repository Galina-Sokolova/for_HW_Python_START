class BasicException(Exception):
    pass


class LevelError(BasicException):
    def __init__(self, u_level, a_level):
        self.u_level = u_level
        self.a_level = a_level

    def __str__(self):
        return f"Недостаточный уровень доступа <{self.a_level}>! Требуемый уровень: <{self.u_level}>."


class AccessError(BasicException):
    def __init__(self, u_name, u_id):
        self.u_name = u_name
        self.u_id = u_id

    def __str__(self):
        return f'User name: <{self.u_name}>, id: <{self.u_id}> - нет в списке пользователей!'


# class LevelValueError(BasicException):
#     def __init__(self, min_val, max_val):
#         self.min_val = min_val
#         self.max_val = max_val
#
#     def __str__(self):
#         return f'Уровень пользователя должен быть в диапазоне {self.min_val} - {self.max_val - 1}!'

