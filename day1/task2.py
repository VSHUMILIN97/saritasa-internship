import logging
logging.basicConfig(level=logging.DEBUG)
first = {'id': 15, 'uno': 1, 'bottle': 'neck'}
second = {'id': 12, 'duos': 2, 'bottle': 'wine'}


def check_and_merge_my_dict(dict1, dict2):
    inner_keys = list(dict1.keys())
    for item in inner_keys:
        if dict2.get(item) is not None:
            logging.info('Warning, key - ' + item + ' is doubled')
    dict1.update(dict2)
    return dict1


if __name__ == '__main__':
    print(check_and_merge_my_dict(first, second))
