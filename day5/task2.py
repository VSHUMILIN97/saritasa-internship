"""
TO-DO:
    * In-place operations
    * ?
"""
import copy


class MimicMatrix:
    """ Class that mimic Matrix behviour and supports basic operations

    Attributes:
        matrix (list): Matrix-like structure to iterate through
    """
    __slots__ = ['matrix', 'm_size']

    def __init__(self, matrix):
        self.matrix = [x for x in matrix]
        self.m_size = (len(self.matrix), 0)
        self.check_size()

    def check_size(self):
        """ Checking size of the current Matrix

        Returns:
            None
        """
        if self.m_size[0] == 0:
            raise ValueError('Put dimensions to matrix')
        for matrix_index, _ in enumerate(self.matrix):
            if len(self.matrix[matrix_index]) != \
                    len(self.matrix[matrix_index - 1]):
                raise ValueError('Rows are not the same size')
        self.m_size = (len(self.matrix), len(self.matrix[0]))

    def _is_matrix_compatible(self, matrix):
        """ Checks whether matrix are compatible

        Args:
            matrix (MimicMatrix): Another Matrix instance

        Returns:
            bool: True for if Matrix object is compatible
        """
        if not isinstance(matrix, MimicMatrix):
            raise TypeError('Not Matrix instance')
        if self.m_size != matrix.m_size:
            raise ValueError('Matrix instances are not the same size')
        return True

    def _is_matrix_mul_compatible(self, matrix):
        """ Function checks whether matrix is compatible for
            multiplying by number or another matrix

        Args:
            matrix (object): Can be int or MimicMatrix type.

        Returns:
            bool: True if it is MimicMatrix object, False if int.
            Raises TypeError object otherwise.
        """
        if isinstance(matrix, int):
            return False
        if not isinstance(matrix, MimicMatrix):
            raise TypeError('Not Matrix instance')
        if self.m_size != tuple(reversed(matrix.m_size)):
            raise TypeError('Matrix instances cannot be multiplied')
        return True

    def __add__(self, other_matrix):
        """ Magic method that mimic Matrix addition

        Args:
            other_matrix: MimicMatrix

        Returns:
            list: In-place operation of addition
        """
        if self._is_matrix_compatible(other_matrix):
            rows, values = self.m_size
            addition_matrix = [[self.matrix[row][value] + other_matrix[row][value]
                                for value in range(values)]
                               for row in range(rows)]
            return addition_matrix

    def __radd__(self, other_matrix):
        """ Magic method that mimic Matrix addition

        Notes:
            In any cases you would not be able to add anything else,
            but MimicMatrix to MimicMatrix, so it is just a stab
        """
        return self.__add__(other_matrix)

    def __getitem__(self, index):
        """ Simply returns item from matrix by given index """
        return self.matrix[index]

    def __sub__(self, other_matrix):
        """ Magic method that mimic Matrix subtraction

        Args:
            other_matrix: MimicMatrix

        Returns:
            list: In-place operation of subtraction
        """
        if self._is_matrix_compatible(other_matrix):
            rows, values = self.m_size
            subtracted_matrix = [[self.matrix[row][value] - other_matrix[row][value]
                                  for value in range(values)]
                                 for row in range(rows)]

            return subtracted_matrix

    def __rsub__(self, other_matrix):
        """ Magic method that mimic Matrix subtraction

        Notes:
            In any cases you would not be able to sub anything else,
            but MimicMatrix to MimicMatrix, so it is just a stab
        """
        return self.__sub__(other_matrix)

    def __neg__(self):
        """ Magic method that mimic Matrix negation operation """
        return self.__mul__(-1)

    def __imul__(self, other_matrix):
        """ In-place multiplication """
        result = self.__mul__(other_matrix)
        return result

    def __iadd__(self, other_matrix):
        """ In-place addition """
        result = self.__add__(other_matrix)
        return result

    def __isub__(self, other_matrix):
        """ In-place subtraction """
        result = self.__sub__(other_matrix)
        return result

    def __mul__(self, other_matrix_or_num):
        """ Magic method that mimic Matrix multiplication
            It iterates through Matrix by this algorithm:
                (1, 2),    x     (3, 4),
                (3, 4)     x     (5, 6)
                ------------------------
                (1, 2) x (3),  ->  (1, 2) x (4),   ->  Same to the second
                         (5)   ->           (6)    ->  raw

                ------------------------
                (1, 2),               (1 |x2, 2 |x2),
                (    )   x  2   ->    (            )
                (3, 4)                (3 |x2, 4 |x2)
        Args:
            other_matrix_or_num: MimicMatrix or int type value

        Returns:
            list: Result of multiplication
        """
        if self._is_matrix_mul_compatible(other_matrix_or_num):
            other_matrix_or_num = list(zip(*other_matrix_or_num))
            new_structure = []
            state = []
            counter = 0
            rows, values = self.m_size
            for row in range(rows):
                for tuple_len, _ in enumerate(other_matrix_or_num):
                    for value in range(values):
                        counter += self.matrix[row][value] * \
                                   other_matrix_or_num[tuple_len][value]
                    new_structure.append(counter)
                    counter = 0
                state.append(copy.copy(new_structure))
                new_structure.clear()
            return state
        else:
            copyr = copy.copy(self.matrix)
            rows, values = self.m_size
            for row in range(rows):
                for value in range(values):
                    copyr[row][value] *= other_matrix_or_num
            return copyr

    def __pow__(self, number):
        """ Magic method that mimic operation of involution """
        if isinstance(number, int):
            matrix = None
            columns, rows = self.m_size
            if columns != rows:
                raise TypeError('Unsupported matrix type (must be square)')
            for _ in range(number - 1):
                matrix = self.__mul__(MimicMatrix(self.matrix))
            return matrix
        else:
            raise TypeError(f'Cannot involute on - {type(number)} type')

    def transpose(self):
        """ Mimic transpose operation

        References:
             https://en.wikipedia.org/wiki/Transpose
        """
        return [list(x) for x in zip(*self.matrix)]

    def __repr__(self):
        return str(self.matrix)


if __name__ == '__main__':
    pass
