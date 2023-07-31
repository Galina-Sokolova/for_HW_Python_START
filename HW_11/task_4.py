# Создайте класс Матрица. Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
class Matrix:

    def __init__(self, matrix: list[list[int]]):
        self._rows = len(matrix)
        self._cols = len(matrix[0])
        self._matrix = matrix

    def __add__(self, other):
        """Calculates the sum of matrices"""
        if not isinstance(other, self.__class__):
            raise TypeError("The object does not belong to the Matrix class")
        if self._cols != other._cols or self._rows != other._rows:
            raise ValueError('The operation cannot be performed for matrices of different dimensions')
        sum_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._cols):
                sum_matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(sum_matrix)

    def __mul__(self, other):
        """Calculates a multiplication of matrices"""
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._cols != other._rows:
            raise ValueError(
                "The number of rows of the first matrix is not equal to the number of columns of the second matrix")
        mult_matrix = [[0 for _ in range(other._cols)] for _ in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._cols):
                for k in range(self._cols):
                    mult_matrix[i][j] += self._matrix[i][k] * other._matrix[k][j]
        return Matrix(mult_matrix)

    def __eq__(self, other) -> bool:
        """Returns True if the matrix equals to other one"""
        return self._matrix == other._matrix

    def __str__(self):
        """User-readable representation method"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix]) + '\n'

    def __repr__(self):
        """String object representation method"""
        return f'Matrix({self._matrix})'


if __name__ == '__main__':
    matrix_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    matrix_c = Matrix([[1, 2, 3], [2, 3, 4]])
    matrix_d = Matrix([[1, 2], [3, 4], [1, 5]])
    print(f'matrix_a = \n{matrix_a}')
    print(f'matrix_b = \n{matrix_b}')
    print(f'matrix_a + matrix_b  = \n{matrix_a + matrix_b}')
    print(f'matrix_c = \n{matrix_c}')
    print(f'matrix_d = \n{matrix_d}')
    print(f'matrix_c * matrix_d  = \n{matrix_c * matrix_d}')
    print(f'matrix_a == matrix_b is {matrix_a == matrix_b}')
    print(f'matrix_c == matrix_d is {matrix_c == matrix_d}')
    print(f'{matrix_d = }')

