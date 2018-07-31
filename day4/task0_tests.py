import unittest
from day4.task0 import YRange


class IterationTest(unittest.TestCase):

    def test_always_zero_on_negative_value(self):
        """Test that checks whether start value is always 0
           if input is negative integer
        """
        bbox = YRange(-1)
        self.assertEqual(0, bbox.start)

    def test_endpoint_is_always_bigger(self):
        """Test that checks whether endpoint less than iteration
           value or not
        """
        bbox = YRange(2)
        for _ in range(10**5):
            self.assertGreater(2, bbox.start)

    def test_float_is_correctly_iterating(self):
        """Test that checks that float is treated like an integer
        """
        bbox = YRange(2.9)
        self.assertEqual(1, next(bbox))
        self.assertEqual(2, next(bbox))
        self.assertEqual(0, next(bbox))
        self.assertEqual(1, next(bbox))
