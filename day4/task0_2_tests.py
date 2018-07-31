import unittest
from day4.task0_2 import SimpleGenerator, \
                         simple_gen


class IterationTest(unittest.TestCase):

    def test_always_zero_on_negative_value(self):
        """Test that checks whether start value is always 0
           if input is negative integer
        """
        bbox = SimpleGenerator(-1)
        self.assertEqual(0, bbox.start)
        funcbbox = simple_gen(-1)
        with self.assertRaises(StopIteration):
            next(funcbbox)

    def test_endpoint_is_always_bigger(self):
        """Test that checks whether endpoint less than iteration
           value or not
        """
        bbox = SimpleGenerator(2)
        for _ in range(10**5):
            self.assertGreater(2, bbox.start)
        funcbbox = simple_gen(2)
        for _ in range(10**5):
            self.assertGreater(2, next(funcbbox))
