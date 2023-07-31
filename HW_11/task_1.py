# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time, strftime, gmtime


class MyStr(str):
    """Сlass extending class str with new attributes"""

    def __new__(cls, value, autor):
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.start_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return f'Автор строки {self =}: {self.autor}, время создания {self.start_time}'
        # return str({"value": self} | self.__dict__)

    # def __repr__(self):
    #     #return f'Автор строки {self =}: {self.autor}, время создания {self.start_time}'
    #     return str({"value": self} | self.__dict__)


s_1 = MyStr('First', 'Petrov')
print(s_1)
s_2 = MyStr('Second', 'Simonova')
print(s_2)
#print(repr(s_2))
