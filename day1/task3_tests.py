"""This module contains tests for the task3

It demonstrates behaviour of the app and how it should be used.
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Validate template strings for given context
"""
import unittest
from unittest import mock
from day1.task3 import build_string


class ValidatorTest(unittest.TestCase):

    def test_validation_passes_with_all_params(self):
        """This test checks whether string is built or not

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=build_string)
        func_from_mock = mock_obj()
        self.assertIsInstance(func_from_mock({'name': 'Let',
                                              'age': 'down',
                                              'workplace': 'you',
                                              'quote': 'dirty',
                                              'marriage': 'rabbit'},
                                             '{name} me {age}'), str)

    def test_validation_exit_with_wrong_input(self):
        """This test check whether system shutdown with code 1 or
           raises an exception

        Returns:
            The return value. True for success, False otherwise.
        """
        mock_obj = mock.MagicMock(name='min',
                                  return_value=build_string)
        func_from_mock = mock_obj()
        with self.assertRaises(SystemExit) as exit_manager:
            func_from_mock({'context': 'me'}, '{context}')

        self.assertEqual(exit_manager.exception.code, 1)
