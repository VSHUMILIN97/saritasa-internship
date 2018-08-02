"""
TO-DO:
    * Split tests
    * Write more tests
"""

import unittest
from day5.task1 import SetLike


class SetLikeObjectTest(unittest.TestCase):
    """ This tests are written for proper studying of
        SetLike objects
    """

    def test_that_checks_on_building_set(self):
        """ Check that it is possible to build a SetLike object """
        a = SetLike([1, 2, 3, 3, 15])
        b = SetLike([1, 2, 4, 5])
        self.assertListEqual(sorted(a.unique), [1, 2, 3, 15])
        self.assertEqual(sorted(b.unique), [1, 2, 4, 5])

    def test_adding_values_to_set(self):
        a = SetLike([1, 2, 3, 3, 15])
        b = SetLike([1, 2, 4, 5])
        a.add(12)
        b.add(12)
        b.add(3)
        b.add([10, 9])
        print()
        self.assertListEqual(sorted(a.unique), [1, 2, 3, 12, 15])
        self.assertListEqual(sorted(b.unique), [1, 2, 3, 4, 5, 9, 10, 12])

    def test_check_implementation_of_basic_operations(self):
        """ SetLike Basic operations """
        a = SetLike([1, 2, 3])
        b = SetLike([1, 2, 4, 5])
        self.assertListEqual(sorted(a & b), [1, 2])
        self.assertListEqual(sorted(a | b), [1, 2, 3, 4, 5])
        self.assertListEqual(sorted(a - b), [3])

    def test_check_implementation_of_eqaulity_operations(self):
        """ SetLike eqaulity operators """
        a = SetLike([1, 2, 3, 4, 5, 6])
        b = SetLike([1, 2, 4, 5])
        self.assertTrue(a >= b)
        self.assertTrue(a > b)
        self.assertFalse(a < b)
        self.assertFalse(a != b)
        self.assertFalse(a <= b)
        self.assertFalse(a == b)


