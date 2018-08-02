"""
    TO-DO:
    * Unit tests
"""
import time
from functools import wraps

""" This function is stub for fetching argument which are
    exceptions, retries and delay

Args:
    exceptions: The exception to check. may be a tuple of
        exceptions to check.
    retries: Number of times to try (not retry) before giving up.
    delay: Initial delay between retries in seconds.

Returns:
    object: The result of decorated function by chain
"""


def retry(exceptions, retries=None, delay=3):
    def d_retry(func):
        """ Real decorator which handle function arguments and
            result of its work.

        Args:
            func: function to decorate

        Returns:
            object: The result of decorated function
        """
        @wraps(func)
        def f_retry(*args, **kwargs):

            user_retries, user_delay = retries, delay
            if user_retries is None:
                user_retries = True
            else:
                user_retries -= 1
            while user_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    msg = f'{e} Retrying in {user_delay} second(s)...'
                    print(msg)
                    time.sleep(user_delay)
                    if user_retries is True:
                        continue
                    user_retries -= 1
            return func(*args, **kwargs)
        return f_retry
    return d_retry


if __name__ == '__main__':
    pass

