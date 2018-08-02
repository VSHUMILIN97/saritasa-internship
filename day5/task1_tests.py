import unittest
from day5.task1 import SetLike


class SetLikeObjectTest(unittest.TestCase):
    """ This tests are written for proper studying of
        SetLike objects
    """

    def test_that_checks_all_basic_attributes(self):
        a = SetLike([1, 2, 3, 3, 15])
        b = SetLike([1, 2, 4, 5])
        self.assertListEqual(sorted(a.unique), [1, 2, 3, 15])
        a.add(12)
        b.add(12)
        b.add(3)
        a += {11}
        self.assertListEqual(sorted(a.unique), [1, 2, 3, 11, 12, 15])
        self.assertListEqual(sorted(a & b), [1, 2, 3, 12])
        self.assertListEqual(sorted(a | b), [1, 2, 3, 4, 5, 11, 12, 15])
        self.assertListEqual(sorted(a - b), [11, 15])
        a.add(10)
        b.add(1)
        self.assertListEqual(sorted(a ^ b),
                             [1, 2, 3, 4, 5, 10, 11, 12, 15])
        self.assertFalse(a >= b)
        self.assertFalse(a > b)
        self.assertFalse(a < b)
        self.assertTrue(a != b)
        self.assertFalse(a == b)
        a &= b
        self.assertListEqual(sorted(a), [1, 2, 3, 12])
        a |= b
        self.assertListEqual(sorted(a), [1, 2, 3, 4, 5, 12])

    def test_that_checks_all_methods(self):
        a = SetLike([1, 2, 3, 3])
        b = SetLike([1, 5])
        self.assertListEqual(sorted(a.intersection(b)), [1])
        self.assertIsNone(a.clear())
        with self.assertRaises(KeyError) as cm:
            a.pop(1)
        self.assertEqual(cm.exception,
                         'No more elements in this beautiful set')
        self.assertEqual(sorted(b), [1, 5])
        self.assertFalse(sorted(b.issubset(a)))
