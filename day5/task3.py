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
                    glob_list.append(each_val)
    except TypeError:
        raise SystemExit('Wrong input type')
    return glob_list


if __name__ == '__main__':
    first = [1, 2, 3, 4]
    second = (i ** 2 for i in range(5))
    third = range(10)
    fourth = 'Kappa'
    fifth = {10, 20, 30, 40}
    print(concatenate_sequence(first, second, third, fourth, fifth))
