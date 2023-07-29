# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, width: int | float, height: int | float | None = None):
        self._width = width
        self._heigth = height or width

    def perimeter(self) -> float:
        return 2 * (self._width + self._heigth)

    def area(self) -> float:
        return self._width * self._heigth

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Not a "Rectangle" instance')
        ratio_width = self._width / self.perimeter()
        ratio_height = self._heigth / self.perimeter()
        new_perimetr = self.perimeter() + other.perimeter()
        return Rectangle(new_perimetr * ratio_width, new_perimetr * ratio_height)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('Not a "Rectangle" instance')
        ratio_width = self._width / self.perimeter()
        ratio_height = self._heigth / self.perimeter()
        new_perimetr = abs(self.perimeter() - other.perimeter())
        return Rectangle(new_perimetr * ratio_width, new_perimetr * ratio_height)

    def __eq__(self, other):
        """равны ли площади"""
        return self.area() is other.area()

    def __ne__(self, other):
        """не равны ли площади"""
        return self.area() is not other.area()

    def __gt__(self, other):
        """больше ли площади"""
        return self.area() > other.area()

    def __lt__(self, other):
        """меньше ли площади"""
        return self.area() < other.area()

    def __str__(self):
        return (f'\nRectangle:\n{self._width} x {self._heigth}'
                f'\nPerimetr: {self.perimeter()}'
                f'\nArea:     {self.area()}')

    def __repr__(self):
        return f'Rectangle({self._width}, {self._heigth})'


if __name__ == '__main__':
    rectangle_1 = Rectangle(10, 20)
    rectangle_2 = Rectangle(14, 7)
    rectangle_3 = rectangle_1 + rectangle_2
    print(rectangle_3)
    print(f'{rectangle_3 = }')