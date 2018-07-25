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
                for key in range(0, len(keys)):
                    custom_dict.setdefault(keys[key], row[key])
                listing.append(custom_dict)
        return listing, keys
    except IOError:
        logging.error('Cannot reach the file')
        exit(0)


def count_entries(generated_list, keys):
    """
    Function counts and composes dicts for every special keyword

    :param generated_list: list object that stores all objects from csv file
    :param keys: list object that stores all header keywords from csv file
    :return:
        dict: contains links between keys and prepared data
        keys: contains header of the csv file. First line is for the keywords
    """
    entries_storage = {}
    for key in keys:
        entries_storage[key] = None
        parsed_values = []
        for every_dict in generated_list:
            for key1, val in every_dict.items():
                if key1 == key:
                    parsed_values.append(val)
        entries_storage[key] = parsed_values
    return entries_storage, keys


def extending_data_with_keywords(generated_dict, keys):
    """
    This function uses collection.Counter class object
    to create a special dict with parsed counters

    :param generated_dict: dict object that stores {key: list with values}
    :param keys: list object that stores all header keywords from csv file
    :return:
        list: object that contains dicts with our representation of the file
    """
    core_list = []
    for key in keys:
        mama = collections.Counter(generated_dict[key])
        for key1, val in mama.items():
            core_list.append({'key': key, 'value': key1, 'count': val})
    return core_list


def get_arguments():
    """
    Function that fetch arguments from the command line

    :return:
        string: contains path to csv file (or may be char symbols)
        NOTE: The app will stop if the path is incorrect
    """
    parser = argparse.ArgumentParser(description='Process file path')
    parser.add_argument('path', metavar='P', type=str,
                        help='a string contains absolute path to file')
    return parser.parse_args()


if __name__ == '__main__':
    parse_result = parse_csv(get_arguments())
    parsed_dict, keywords = count_entries(parse_result[0], parse_result[1])
    logging.info(extending_data_with_keywords(parsed_dict, keywords)[-1::-1])
