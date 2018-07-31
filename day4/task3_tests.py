import unittest
from day4.task3 import concatenate_sequence, ConcatSequence


class SingletonTest(unittest.TestCase):

    def test_concat_is_true(self):
        """Test that concatenation is right in both func and cls
        """
        cs = ConcatSequence([1, 2], {3, 4})
        new_list = []
        for x in cs:
            new_list.append(x)
        cs_func = concatenate_sequence([1, 2], {3, 4})
        self.assertEqual(next(cs_func), new_list[0])

    def test_incorrect_input_is_handled_by_class(self):
        """Test that checks whether class method handle
           incorrect input
        """
        with self.assertRaises(SystemExit) as cm:
            for _ in ConcatSequence(1):
                pass
        self.assertEqual('Wrong input type', cm.exception.code)

    def test_incorrect_input_is_handled_by_function(self):
        """Test that checks whether function handle incorrect input
        """
        with self.assertRaises(SystemExit) as cm:
            for _ in concatenate_sequence(1):
                pass
        self.assertEqual('Wrong input type', cm.exception.code)
