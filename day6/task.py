import time
from functools import wraps
import random
"""
    TO-DO:
    * Unit tests
    * Infinite handle
"""


def retry(exceptions, retries=None, delay=3):
    """ This function is decorator which handle fetched
        exceptions and retries function as much, as user
        prefer

    Args:
        exceptions: The exception to check. may be a tuple of
            exceptions to check.
        retries: Number of times to try (not retry) before giving up.
        delay: Initial delay between retries in seconds.
    """
    def deco_retry(func):
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
                    user_retries -= 1
            return func(*args, **kwargs)
        return f_retry
    return deco_retry


if __name__ == '__main__':
    @retry((KeyError, ValueError), delay=1, retries=12)
    def sample():
        if random.random() < 0.5:
            raise ValueError('What did you expect?')
        elif 0.5 < random.random() < 0.90:
            raise KeyError('A real test?')
        else:
            print('Success')
    sample()

