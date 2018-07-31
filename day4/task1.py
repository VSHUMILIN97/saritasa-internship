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
        # Can be like reversed(list(seq)) - I know, but not cool
        seq = tuple(seq)
        print(f'Default - {seq}')
        output_sec = []
        for minus in range(0, len(seq)):
            output_sec.append(seq[-minus - 1])
        return output_sec
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


def rseq_factory(sec):
    reversed_seq = RSequence(sec)
    for each_value in reversed_seq:
        pprint.pprint(each_value)


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 6, 7, 8]
    string_sequence = 'Privet'
    pprint.pprint(f'Reverse - {reverse_iter(sequence)}')
    pprint.pprint(f'Reverse - {reverse_iter(string_sequence)}')

    line = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    for _ in range(5):
        print(f'{line}ENDPOINT FUNC CALL{line}')
        time.sleep(0.5)

    rseq_factory(sequence)
    rseq_factory(string_sequence)
