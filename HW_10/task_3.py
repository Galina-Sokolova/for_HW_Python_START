# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
class CharacterRepetition:

    def __init__(self):
        self.text = input("Input text:  ")

    def most_common_character(self):
        text = self.text.translate(str.maketrans({'-': ' ', '.': '', ',': '', '—': ''})).split()
        result = {}
        for i in text:
            if i.lower() in result.keys():
                result[i.lower()] += 1
            else:
                result[i.lower()] = 1
        result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        return result[:5]


new_text = CharacterRepetition()
print(new_text.most_common_character())
