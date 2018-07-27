"""This script merging two dicts by keys.
   It displays a warning in case if dicts contains duplicating keys
"""
import logging
logging.basicConfig(level=logging.DEBUG)
first = {'id': 15, 'uno': 1, 'bottle': 'neck'}
second = {'id': 12, 'duos': 2, 'bottle': 'wine'}


def check_and_merge_my_dict(dict1, dict2):
    """Function that compares keys of both dicts

    It checks whether there are common keys for
    two dictionaries, warning if so and merge them anyways

    Args:
        dict1 (dict): dictionary from user
        dict2 (dict): dictionary from user

    Returns:
        dict: dictionary that contains all the merged data
    """
    try:
        for key in dict1.keys():
            if key in dict2.keys():
                logging.info(f"Current key - '{key}' is doubled")
        dict1.update(dict2)
        return dict1
    except AttributeError:
        logging.error('Incorrect data type. Shutting down')
        return exit(1)


if __name__ == '__main__':
    print(check_and_merge_my_dict(first, second))
