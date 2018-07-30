import time
import pprint


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


for each_iter in simple_gen(5):
    pprint.pprint(each_iter)
    time.sleep(0.5)

