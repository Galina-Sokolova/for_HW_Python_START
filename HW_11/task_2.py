# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра
class Archive:
    """Класс Архив, который хранит пару свойств: число и строку. Ранее созданные экземпляры храняться в list-архивах"""
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arg = []
        else:
            cls._instance.list_arg.append((cls._instance.number, cls._instance.text))
        return cls._instance

    def __init__(self, number: int, text: str):
        self.number = number
        self.text = text

    def __str__(self):
        return f'For user: {self.number = }, {self.text = }, {self.list_arg = }'

    def __repr__(self):
        return f'Archive({self.number}, "{self.text}")'


print(Archive.__doc__)
inst_1 = Archive(1, 'text1')
print(inst_1)
inst_2 = Archive(2, 'text2')
print(inst_2)
inst_3 = Archive(3, 'text3')
print(inst_3)
print(f'{inst_3 = }')
