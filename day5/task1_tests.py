import unittest
from day5.task1 import reverse_iter, RSequence


class ReverseTest(unittest.TestCase):

    def test_data_is_reversed_by_class(self):
        """Test that checks whether data is reversed
           by class
        """
        storage = []
        bbox = RSequence([1, 2, 3])
        for item in bbox:
            storage.append(item)
        self.assertEqual([3, 2, 1], storage)
        storage.clear()
        textbbox = RSequence('Hi')
        for item in textbbox:
            storage.append(item)
        self.assertEqual('iH', ''.join(storage))

    def test_endpoint_is_always_bigger(self):
        """Test that checks whether data is reversed
           by func
        """
        storage = []
        for item in reverse_iter([1, 2, 3]):
            storage.append(item)
        self.assertEqual([3, 2, 1], storage)
        storage.clear()
        textbbox = 'Mark'
        for item in textbbox:
            storage.append(item)
        self.assertEqual('kraM', ''.join(textbbox))

    def test_function_return_reversed_iterator(self):
        self.assertIsInstance(reverse_iter([1]), iter)
