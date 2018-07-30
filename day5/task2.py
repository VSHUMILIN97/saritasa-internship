def singleton(class_):
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


if __name__ == '__main__':
    first = OneGenerator()
    for _ in range(3):
        print(next(first))
    second = OneGenerator()
    print(next(second))
