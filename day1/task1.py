"""This script performing csv parsing,
   then counting any entries of the objects
"""
import csv
import logging
import argparse
import collections
logging.basicConfig(level=logging.DEBUG)


def parse_csv(path_to_file):
    """
    Function parses csv documents for keys and data

    :param path_to_file: string object which is path to the csv document
    :return:
        list: contains dictionaries with parsed data
        keys: contains header of the csv file. First line is for the keywords
    """
    listing = []
    try:
        with open(path_to_file.path, 'r') as csvfile:
            key_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            keys = next(key_reader)
            for row in key_reader:
                custom_dict = {}
                for key in enumerate(keys):
                    custom_dict.setdefault(keys[key[0]], row[key[0]])
                listing.append(custom_dict)
        return listing, keys
    except IOError:
        logging.error('Cannot reach the file')
        exit(0)


def count_entries(generated_list, keyword_list):
    """
    Function counts and composes dicts for every special keyword

    :param generated_list: list object that stores all objects from csv file
    :param keyword_list: list object that stores all header keywords from
           csv file
    :return:
        dict: contains links between keys and prepared data
        keys: contains header of the csv file. First line is for the keywords
    """
    entries_storage = {}
    for key in keyword_list:
        entries_storage[key] = None
        parsed_values = []
        for every_dict in generated_list:
            for child_key, val in every_dict.items():
                if child_key == key:
                    parsed_values.append(val)
        entries_storage[key] = parsed_values
    return entries_storage, keyword_list


def extending_data_with_keywords(generated_dict, keyword_list):
    """
    This function uses collection.Counter class object
    to create a special dict with parsed counters

    :param generated_dict: dict object that stores {key: list with values}
    :param keyword_list: list object that stores all header keywords from
           csv file
    :return:
        list: object that contains dicts with our representation of the file
    """
    core_list = []
    for keyword in keyword_list:
        counter = collections.Counter(generated_dict[keyword])
        for child_key, val in counter.items():
            core_list.append({'key': keyword, 'value': child_key,
                              'count': val})
    return core_list


def get_arguments():
    """
    Function that fetch arguments from the command line

    :return:
        string: contains path to csv file (or may be char symbols)
        NOTE: The app will stop if the path is incorrect
    """
    parser = argparse.ArgumentParser(description='Process file path')
    parser.add_argument('path',
                        metavar='P',
                        type=str,
                        help='a string contains absolute path to file')
    return parser.parse_args()


if __name__ == '__main__':
    dictionaries, main_keys = parse_csv(get_arguments())
    parsed_dict, keywords = count_entries(dictionaries, main_keys)
    logging.info(extending_data_with_keywords(parsed_dict, keywords)[-1::-1])
