"""
ADD MATRIX STUFF
"""


class MimicMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.m_size = (len(matrix), 0)
        self.check_size()

    def check_size(self):
        """ Checking size of the current Matrix

        Returns:
            None
        """
        if self.m_size[0] == 0:
            raise ValueError('Put dimensions to matrix')
        for matrix_index in range(len(self.matrix)):
            for row_index in range(len(self.matrix[matrix_index])):
                print(self.matrix[matrix_index][row_index])
            print()

    def is_matrix_compatible(self, matrix):
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

    def __add__(self, other):
        pass


a = MimicMatrix([[1, 2, 3], [5, 6, 7]])
a.check_size()
