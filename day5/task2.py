import time


LINE = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
ENDPOINT = 'ENDPOINT CLASS CALL'
instances = {}


def singleton(class_):
    """Decorator that returns instance in Singleton pattern

    Args:
        class_ (cls): Checks for the class name

    Returns:
        Result of inner function
    """
    def get_instance(*args, **kwargs):
        """Save the instance in the global dictionary

        Args:
            *args: everything from input function
            **kwargs: everything from input function

        Returns:
            Instance of the input class/function
        """
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class OneGenerator:
    """This class return single instance of Basic Generator
    """
    def __init__(self):
        self.dummy_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.dummy_value += 1
        return self.dummy_value


@singleton
def one_generator():
    """Implementation of Simple generator w/ counter

    Yields:
        int: Counter of current iteration
    """
    counter = 1
    while True:
        yield counter
        counter += 1


if __name__ == '__main__':
    first = OneGenerator()
    for _ in range(3):
        print(next(first))
    second = OneGenerator()
    print(f'{LINE}NEXT CALL{LINE}')
    print(next(second))

    for _ in range(3):
        print(f'{LINE}{ENDPOINT}{LINE}')
        time.sleep(0.5)

    third = one_generator()
    for _ in range(3):
        print(next(third))
    fourth = one_generator()
    print(f'{LINE}NEXT CALL{LINE}')
    print(next(fourth))
