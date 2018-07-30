import time
import pprint


class SimpleGenerator:
    """This class presents a standard realisation of generator object

    Attributes:
        endpoint (int): User break cycle for the generator
    """
    def __init__(self, endpoint):
        self.start = 0
        self.endpoint = int(endpoint)

    def __iter__(self):
        while self.start < int(self.endpoint):
            if self.start + 1 < self.endpoint:
                yield self.start
                self.start += 1
            else:
                yield self.start
                self.start = 0


def simple_gen(endpoint):
    """This is simple generator func which is endless
       because of ignoring StopIteration error

    Args:
        endpoint (int): Endpoint to the loop cycle

    Returns:
        yield value for each next() generator call
    """
    start = 0
    while start < int(endpoint):
        if start + 1 < endpoint:
            yield start
            start += 1
        else:
            yield start
            start = 0


if __name__ == '__main__':
    real_counter = 0
    for each_iter in simple_gen(5):
        if real_counter < 50:
            pprint.pprint(each_iter)
            time.sleep(0.1)
        else:
            break
        real_counter += 1

    line = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for _ in range(5):
        print(f'{line}ENDPOINT FUNC CALL{line}')
        time.sleep(0.5)

    gen_simple_obj = SimpleGenerator(5)
    for each_iter in gen_simple_obj:
        pprint.pprint(each_iter)
        time.sleep(0.1)
