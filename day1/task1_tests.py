"""This module contains tests for the task1

It demonstrates behaviour of the app and how it should be used.
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Parse CSV file and then count matches
"""
import unittest
from unittest import mock
from day1.task1 import get_arguments, extending_data_with_keywords as ext_dt, \
                       count_entries as c_e


class CountMatchesTest(unittest.TestCase):

    def test_crash_on_wrong_input(self):
        """This test checks whether app is reacting on the incorrect
           path input
        """
        mock_obj = mock.MagicMock(
            name='min',
            return_value=get_arguments
        )
        mocking_func = mock_obj()
        with self.assertRaises(SystemExit) as cm:
            mocking_func(['/some/related/path'])
        self.assertEqual(cm.exception.code, 1)

    def test_extending_data_with_keywords(self):
        """This test checks whether it is possible to extend the list
           with given criteria
        """
        attribute_dict = {1: [1 in range(50)],
                          2: [1 in range(100)]}
        self.assertIsInstance(ext_dt(attribute_dict, [1, 2])[0], dict)
        self.assertIsInstance(ext_dt(attribute_dict, [1, 2]), list)
        self.assertEqual(ext_dt(attribute_dict, [1, 2])[0]['value'], 1)

    def test_storage_data_in_dictionaries(self):
        """This test checks whether it is possible to storage data
           in the dictionary
        """
        prepared_data = [{1: 3, 2: 4}, {1: 5, 2: 6}]
        keys = [1, 2]
        self.assertEqual(c_e(prepared_data, keys)[1], keys)
        self.assertEqual(c_e(prepared_data, keys)[0][1], [3, 5])

    def test_count_return_true_value(self):
        result = ext_dt({1: [1, 1, 1, 1, 1]}, [1])
        self.assertEqual({'key': 1, 'value': 1, 'count': 5}, result[0])
