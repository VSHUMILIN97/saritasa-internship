def concatenate_sequence(*args):
    """This function concat every sequence on the entrance
       in the one global list and then output it

    Args:
        *args (seq): User sequences to concatenate

    Returns:
        list: List with the concatenation result
    """
    glob_list = []
    try:
        for each_sequence in args:
                for each_val in each_sequence:
                    yield each_val
                    glob_list.append(each_val)
    except TypeError:
        raise SystemExit('Wrong input type')
    return glob_list


class ConcatSequence:
    """This class support iteration through every sequence
       in the *args list

    Attributes:
        *args (list): List of sequences
    """
    def __init__(self, *args):
        self.sequence_args = args

    def __iter__(self):
        try:
            for each_sequence in self.sequence_args:
                for each_val in each_sequence:
                    yield each_val
        except TypeError:
            raise SystemExit('Wrong input type')


if __name__ == '__main__':
    first = [1, 2, 3, 4]
    second = (i ** 2 for i in range(5))
    third = range(10, 15)
    fourth = 'Kappa'
    fifth = {10, 20, 30, 40}
    cs_with_args = concatenate_sequence(first, second, third, fourth, fifth)
    iterable_func = iter(cs_with_args)
    for any_val in iterable_func:
        print(any_val)
    print(cs_with_args)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    second = (i**2 for i in range(6))
    cs = ConcatSequence(first, second, third, fourth, fifth)
    iterable_cls = iter(cs)
    for any_val in iterable_cls:
        print(any_val)
    print(cs)
