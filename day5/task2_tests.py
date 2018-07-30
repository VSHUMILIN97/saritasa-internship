import unittest
from day5.task2 import OneGenerator, one_generator


class SingletonTest(unittest.TestCase):

    def test_class_is_single_instance(self):
        """Test that class is singleton
        """
        first_inst = OneGenerator()
        self.assertEqual(1, next(first_inst))
        second_inst = OneGenerator()
        self.assertEqual(2, next(second_inst))
        self.assertEqual(first_inst, second_inst)

    def test_endpoint_is_always_bigger(self):
        """Test that function is singleton
        """
        first_inst = one_generator()
        self.assertEqual(1, next(first_inst))
        second_inst = one_generator()
        self.assertEqual(2, next(second_inst))
        self.assertEqual(first_inst, second_inst)






