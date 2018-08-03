import unittest
import day6.task as dt


class DecoratorTest(unittest.TestCase):

    @staticmethod
    def raising_success():
        """ Function that raises success for every initialization """
        @dt.retry((KeyError, ValueError), delay=0.0001, retries=12)
        def sample():
            return 'Success'
        return sample()

    def test_decorator_raising_success(self):
        """ Test that checks if method return success """
        self.assertEqual(self.raising_success(), 'Success')

    def test_decorator_raising_error_after_retry(self):
        """ Test that checks if error is handled """
        self.counter = 0

        @dt.retry(KeyError, retries=3, delay=0.0001)
        def fall_once():
            if self.counter == 0:
                self.counter += 1
                raise KeyError
            else:
                return
        fall_once()
        self.assertEqual(self.counter, 1)

    def test_decorator_falls_to_error_after_several_retries(self):
        """ Test that checks if function actually fails """
        self.counter = 0

        @dt.retry(ValueError, retries=4, delay=0.0001)
        def fall_four_times():
            if self.counter < 4:
                self.counter += 1
                raise ValueError('!')
        with self.assertRaises(ValueError) as cm:
            fall_four_times()

        self.assertEqual(self.counter, 4)
        self.assertEqual(str(cm.exception), '!')

    def test_decorator_handle_multiple_error_types(self):
        """ Test that checks if decorator can handle multiple Error types """
        self.counter = 0

        @dt.retry((ValueError, KeyError), retries=3, delay=0.001)
        def test_handle_multiple_mistakes():
            self.counter += 1
            if self.counter == 1:
                raise ValueError('ValueError drop')
            elif self.counter == 2:
                raise KeyError('KeyError drop')
            else:
                return 'Success'

        self.assertEqual(test_handle_multiple_mistakes(), 'Success')
        self.assertEqual(self.counter, 3)
