import unittest
import day6.task as dt
import random


class DecoratorTest(unittest.TestCase):

    def test_raises_success(self):
        @dt.retry((KeyError, ValueError), delay=0.25, retries=12)
        def sample():
            if random.random() < 0.5:
                raise ValueError('What did you expect?')
            elif 0.5 < random.random() < 0.90:
                raise KeyError('A real test?')
            else:
                print('Success')

        self.assertEqual(sample(), None)
