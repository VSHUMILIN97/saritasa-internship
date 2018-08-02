import unittest
from day5.task2 import MimicMatrix


class MatrixTest(unittest.TestCase):

    def test_matrix_is_same_row_size_and_not_null(self):
        """ Test that checks whether matrix object raises Error
            if its rows are not the same size or null
        """
        with self.assertRaises(ValueError) as cm:
            MimicMatrix([[1, 2, 3], [5, 6]])
        self.assertEqual(str(cm.exception), 'Rows are not the same size')
        with self.assertRaises(ValueError) as cm:
            MimicMatrix([])
        self.assertEqual(str(cm.exception), 'Put dimensions to matrix')

    def test_matrix_are_sub_add_compatible(self):
        """ Test that checks whether matrix object raises Error
            if they are not the same size
        """
        m1m = MimicMatrix([[1, 2, 4], [5, 7, 9]])
        m2m = MimicMatrix([[1, 2, 5], [10, 14, -5]])
        m3m = MimicMatrix([[1, 2], [4, 6]])
        self.assertTrue(m1m._is_matrix_compatible(m2m))
        with self.assertRaises(ValueError) as cm:
            m1m._is_matrix_compatible(m3m)
        self.assertEqual(str(cm.exception),
                         'Matrix instances are not the same size')

    def test_attributes_can_be_fetched_from_instance(self):
        m3m = MimicMatrix([[1, 2], [4, 6]])
        self.assertEqual(m3m.m_size, (2, 2))
        with self.assertRaises(AttributeError) as cm:
            print(m3m.spoon)
        self.assertEqual(str(cm.exception),
                         "'MimicMatrix' object has no attribute 'spoon'")

    def test_matrix_addition_is_possible_and_correct(self):
        """ Test checks whether it is possible to
        """
        m1m = MimicMatrix([[1, 2, 4],
                           [5, 7, 9]])
        m2m = MimicMatrix([[1, 2, 5],
                           [10, 14, -5]])
        obj = m1m + m2m
        self.assertEqual([[2, 4, 9],
                          [15, 21, 4]], obj)

    def test_matrix_substruction_is_possible_and_correct(self):
        m1m = MimicMatrix([[1, 2, 4],
                           [5, 7, 9]])
        m2m = MimicMatrix([[1, 2, 5],
                           [10, 14, -5]])
        obj = m1m - m2m
        self.assertEqual([[0, 0, -1],
                          [-5, -7, 14]], obj)

    def test_multiplication_of_matrix_with_either_matrix_and_number(self):
        """ Test checks whether non-square matrix can be multiplied by number
            or another matrix
        """
        m3m = MimicMatrix([[1, 2, 3],
                           [0, 1, 0]])
        m4m = MimicMatrix([[1, 1],
                           [0, 0],
                           [2, 1]])
        self.assertEqual(m3m*m4m, [[7, 4],
                                   [0, 0]])
        self.assertEqual(m3m*2, [[2, 4, 6],
                                 [0, 2, 0]])

    def test_square_matrix_multiplication(self):
        """ Test checks whether square matrix multiple well"""
        m1m = MimicMatrix([[1, 2],
                           [2, 1]])
        m2m = MimicMatrix([[1, 3],
                           [4, 1]])
        self.assertEqual(m1m*m2m,
                         [[9, 5],
                          [6, 7]])

    def test_involute_matrix_with_bad_or_good_inputs(self):
        """ Test checks whether it is possible to involute matrix"""
        m3m = MimicMatrix([[2, 3],
                           [3, 5]])
        self.assertEqual(m3m**2, [[13, 21],
                                  [21, 34]])
        wrong_mm = MimicMatrix([[1, 2, 8],
                                [3, 4, 5]])
        with self.assertRaises(TypeError) as cm:
            wrong_mm ** 2
        self.assertEqual(str(cm.exception), 'Unsupported matrix type (must be square)')
        with self.assertRaises(TypeError) as cm:
            wrong_mm ** '12'
        self.assertEqual(str(cm.exception), "Cannot involute on - <class 'str'> type")

    def test_matrix_is_transposed(self):
        """ Test checks whether transpose was successful"""
        m3m = MimicMatrix([[1, 2, 3, 4],
                          [5, 6, 7, 8],
                           [9, 10, 11, 12]]).transpose()
        self.assertEqual(m3m,
                         [(1, 5, 9),
                          (2, 6, 10),
                          (3, 7, 11),
                          (4, 8, 12)])

    def test_negate_matrix(self):
        """ Test checks whether it is possible to mul matrix on -1"""
        m3m = MimicMatrix([[2, 3],
                           [3, 5]])
        self.assertEqual(-m3m, [[-2, -3],
                                [-3, -5]])
        m2m = MimicMatrix([[1], [4]])
        nm2m = - m2m
        self.assertEqual(nm2m, [[-1],
                                [-4]])
