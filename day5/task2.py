import time


LINE = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
ENDPOINT = 'ENDPOINT CLASS CALL'


def singleton(class_):
    """

    Args:
        class_ (cls): Checks for the class name

    Returns:

    """
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class OneGenerator:

    def __init__(self):
        self.dummy_value = 0

    def __iter__(self):
        while True:
            yield self.dummy_value
            self.dummy_value += 1

    def __next__(self):
        self.dummy_value += 1
        return self.dummy_value


@singleton
def one_generator():
    _ = 1
    while True:
        yield _
        _ += 1


if __name__ == '__main__':
    first = OneGenerator()
    for _ in range(3):
        print(next(first))
    second = OneGenerator()
    print(LINE)
    print(next(second))

    for _ in range(3):
        print(f'{LINE}{ENDPOINT}{LINE}')
        time.sleep(0.5)

    third = one_generator()
    for _ in range(3):
        print(next(third))
    fourth = one_generator()
    print(next(fourth))
