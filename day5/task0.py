import time
import pprint


class YRange:
    """This class presents a standard realisation of iterator object

    Attributes:
        endpoint (int): User break line for the iteration
    """
    def __init__(self, endpoint):
        self.start = 0
        self.endpoint = int(endpoint)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.endpoint:
            self.start += 1
            return self.start
        else:
            self.start = 0


yrange_object = YRange(5)
for each_iteration in yrange_object:
    pprint.pprint(each_iteration)
    time.sleep(0.5)

