"""This module contains tests for the task1

It demonstrates behaviour of the app and how it should be used.
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Parse CSV file and then count matches
"""
import unittest
from unittest import mock
from day1.task1 import get_arguments, extending_data_with_keywords, \
                       count_entries


class CountMatchesTest(unittest.TestCase):

    def test_getting_arguments(self):
        """This test checks whether it is possible to get the args

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=get_arguments)
        func_from_mock = mock_obj()
        self.assertIsInstance(func_from_mock(['/some/related/path']).path, str)

    def test_extending_data_with_keywords(self):
        """This test checks whether it is possible to extend the list
           with given criteria

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=extending_data_with_keywords)
        func_from_mock = mock_obj()
        attribute_dict = {1: [1 in range(50)],
                          2: [1 in range(100)]}
        self.assertIsInstance(func_from_mock(attribute_dict, [1, 2])[0], dict)
        self.assertIsInstance(func_from_mock(attribute_dict, [1, 2]), list)
        self.assertEqual(func_from_mock(attribute_dict, [1, 2])[0]['value'], 1)

    def test_storage_data_in_dictionaries(self):
        """This test checks whether it is possible to storage data
           in the dictionary

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=count_entries)
        func_from_mock = mock_obj()
        prepared_data = [{1: 3, 2: 4}, {1: 5, 2: 6}]
        keys = [1, 2]
        self.assertEqual(func_from_mock(prepared_data, keys)[1], keys)
        self.assertEqual(func_from_mock(prepared_data, keys)[0][1], [3, 5])
