"""This module contains tests for the task2

It demonstrates behaviour of the app and how it should be used
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Merge two dicts by keys and raise warning for any crosses
"""
import unittest
from day1.task2 import check_and_merge_my_dict as chk_mrg


class DictMergeTest(unittest.TestCase):

    def test_merge_is_completed(self):
        """This test check whether merging was successful or not

        Returns:
            The return value. True for success, False otherwise.
        """
        self.assertTrue({1, 5}, set((chk_mrg(
                                        {1: 2, 3: 4},
                                        {1: 3, 5: 6}).keys())))

    def test_behaviour_after_incorrect_type(self):
        """This test check whether system shutdown with code 1 or
           raises an exception

        Returns:
            The return value. True for success, False otherwise.
        """
        with self.assertRaises(SystemExit) as exit_manager:
            chk_mrg(1, 1)

        self.assertEqual(exit_manager.exception.code, 1)

    def test_merge_unique_dicts(self):
        result = chk_mrg({1: 2, 3: 4}, {5: 6})
        self.assertEqual({1: 2, 3: 4, 5: 6}, result)
