"""
ADD MATRIX STUFF
"""
import copy


class MimicMatrix:

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
        for matrix_index in range(len(self.matrix)):
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
        if isinstance(matrix, int):
            return False
        if not isinstance(matrix, MimicMatrix):
            raise TypeError('Not Matrix instance')
        if self.m_size != tuple(reversed(matrix.m_size)):
            raise TypeError('Matrix instances cannot be multiplied')
        return True

    def __add__(self, other_matrix):
        if self._is_matrix_compatible(other_matrix):
            rows, values = self.m_size
            for row in range(rows):
                for value in range(values):
                    self.matrix[row][value] += other_matrix[row][value]
        else:
            raise TypeError('Unsupported operand type for instances'
                            ' - MimicMatrix and int}')
        return self.matrix

    def __getitem__(self, index):
        return self.matrix[index]

    def __sub__(self, other_matrix):
        if self._is_matrix_compatible(other_matrix):
            rows, values = self.m_size
            for row in range(rows):
                for value in range(values):
                    self.matrix[row][value] -= other_matrix[row][value]
        else:
            raise TypeError('Unsupported operand type for instances'
                            ' - MimicMatrix and int}')
        return self.matrix

    def __getattr__(self, attr):
        if self.__dict__.get(attr) is not None:
            return self.__dict__[attr]
        else:
            raise AttributeError(f'There are no - {attr} in this instance')

    def __mul__(self, other_matrix_or_num):
        if self._is_matrix_mul_compatible(other_matrix_or_num):
            other_matrix_or_num = list(zip(*other_matrix_or_num))
            new_structure = []
            st = []
            counter = 0
            rows, values = self.m_size
            for row in range(rows):
                for tuple_len, _ in enumerate(other_matrix_or_num):
                    for value in range(values):
                        val = self.matrix[row][value] * other_matrix_or_num[tuple_len][value]
                        counter += val
                    new_structure.append(counter)
                    counter = 0
                st.append(copy.copy(new_structure))
                new_structure.clear()
            return st
        else:
            copyr = copy.copy(self.matrix)
            rows, values = self.m_size
            for row in range(rows):
                for value in range(values):
                    copyr[row][value] *= other_matrix_or_num
            return copyr

    def __pow__(self, number, modulo=None):
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
        return list(zip(*self.matrix))

    def __repr__(self):
        return str(self.matrix)


if __name__ == '__main__':
    pass
