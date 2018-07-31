import unittest
from day5.task3 import concatenate_sequence, ConcatSequence


class SingletonTest(unittest.TestCase):

    def test_concat_is_true(self):
        """Test that concatenation is right in both func and cls
        """
        cs = ConcatSequence([1, 2], {3, 4}).concat()
        cs_func = concatenate_sequence([1, 2], {3, 4})
        self.assertEqual(cs, cs_func)

    def test_incorrect_input_is_handled_by_class(self):
        """Test that checks whether class method handle
           incorrect input
        """
        with self.assertRaises(SystemExit) as cm:
            ConcatSequence(1).concat()
        self.assertEqual('Wrong input type', cm.exception.code)

    def test_incorrect_input_is_handled_by_function(self):
        """Test that checks whether function handle incorrect input
        """
        with self.assertRaises(SystemExit) as cm:
            concatenate_sequence(1)
        self.assertEqual('Wrong input type', cm.exception.code)
