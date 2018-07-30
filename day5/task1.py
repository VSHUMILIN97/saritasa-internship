import pprint
import time


def reverse_iter(seq):
    """Function that reverts fetched sequence (easy way)

    Args:
        seq (sequence): Any sequence from user

    Returns:
        sequence: Reversed sequence for the further work
    """
    try:
        seq = reversed(list(seq))
        return seq
    except TypeError:
        raise SystemExit('Unknown data type')


class RSequence:
    """Class which purpose is to reverse sequences

    Attributes:
        seq (sequence): User sequence of data types
    """
    def __init__(self, seq):
        self.seq = list(seq)
        self.length = len(seq)
        self.start = 0

    def __next__(self):
        if self.start < self.length:
            self.start += 1
            return self.seq[-self.start]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 6, 7, 8]
    string_sequence = 'Privet'
    for each_value in reverse_iter(sequence):
        pprint.pprint(each_value)

    line = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for _ in range(5):
        print(f'{line}ENDPOINT FUNC CALL{line}')
        time.sleep(0.5)

    reversed_seq = RSequence(string_sequence)
    for each_value in reversed_seq:
        pprint.pprint(each_value)
