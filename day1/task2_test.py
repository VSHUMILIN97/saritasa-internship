"""This module contains tests for the task2

It demonstrates behaviour of the app and how it should be used
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Merge two dicts by keys and raise warning for any crosses
"""
import unittest
from unittest import mock
from day1.task2 import check_and_merge_my_dict


class DictMergeTest(unittest.TestCase):

    def test_merge_is_completed(self):
        """This test check whether merging was successful or not

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=check_and_merge_my_dict)
        func_from_mock = mock_obj()

        self.assertTrue({1, 5}, set((func_from_mock(
                                        {1: 2, 3: 4},
                                        {1: 3, 5: 6}).keys())))

    def test_behaviour_after_incorrect_type(self):
        """This test check whether system shutdown with code 1 or
           raises an exception

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=check_and_merge_my_dict)
        func_from_mock = mock_obj()
        with self.assertRaises(SystemExit) as exit_manager:
            func_from_mock(1, 1)

        self.assertEqual(exit_manager.exception.code, 1)
