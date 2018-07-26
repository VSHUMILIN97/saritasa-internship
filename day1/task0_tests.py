"""This module contains tests for the task0

It demonstrates behaviour of the app and how it should be used
"""
import locale
import unittest
import string
from unittest import mock
from .task0 import setup_user_environment, transliteration, \
                   get_string_from_user


class TransliterateTest(unittest.TestCase):

    def test_environment_exist(self):
        """This test checks whether users locale contain in real locales

        Returns:
            The return value. True for success, False otherwise.
        """
        exist_locales = locale.locale_alias
        self.assertIn(setup_user_environment().split('.')[0].lower(),
                      exist_locales.keys())

    @mock.patch('builtins.input', side_effect=[''])
    def test_user_prompt_is_string(self, user_input):
        """This test checks whether prompt by user is instance of str or not

        Args:
            user_input (str): User input is showed here.
                              Mocked by unittest.mock module

        Returns:
            The return value. True for success, False otherwise.
        """
        user_prompt = get_string_from_user(setup_user_environment())
        self.assertIsInstance(user_prompt, str)

    @mock.patch('builtins.input', side_effect=['Строка'])
    def test_check_transliteration_is_successful(self, user_input):
        """This test checks whether transliteration works or pass

        Args:
            user_input (str): User input is showed here.
                              Mocked by unittest.mock module

        Returns:
            The return value. True for success, False otherwise.
        """
        output_string = transliteration()
        self.assertEqual(output_string, 'Stroka')

    @mock.patch('builtins.input', side_effect=[string.punctuation])
    def test_check_transliteration_special_symbols(self, user_input):
        """This test checks whether special symbols can pass through or not

        Args:
            user_input (str): User input is showed here.
                              Mocked by unittest.mock module

        Returns:
            The return value. True for success, False otherwise.
        """
        output_string = transliteration()
        self.assertEqual(output_string, string.punctuation)
