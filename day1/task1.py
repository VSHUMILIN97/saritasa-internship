"""This script performing csv parsing,
   then counting any entries of the objects
"""
import csv
import logging
import argparse
import collections
import sys
logging.basicConfig(level=logging.DEBUG)


def parse_csv(path_to_file):
    """Function parses csv documents for keys and data

    Args:
        path_to_file (str): path to the csv document

    Returns:
        list: contains dictionaries with parsed data
        keys: contains header of the csv file. First line is for the keywords
    """
    listing = []
    try:
        with open(path_to_file, 'r') as csvfile:
            key_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            keys = next(key_reader)
            for row in key_reader:
                custom_dict = {}
                for key, _ in enumerate(keys):
                    custom_dict.setdefault(keys[key], row[key])
                listing.append(custom_dict)
        return listing, keys
    except IOError:
        logging.error('Cannot reach the file')
        exit(0)


def count_entries(generated_list, keyword_list):
    """Function counts and composes dicts for every special keyword

    Args:
        generated_list (list): stores all objects from csv file except 1st line
        keyword_list (list): stores all header keywords from csv file

    Returns:
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
    """This function uses collection.Counter class object
       to create a special dict with parsed counters

    Args:
        generated_dict (dict): store pairs like - {key: list with values}
        keyword_list (list): list object that stores all header keywords from
                             csv file

    Returns:
        list: object that contains dicts with our representation of the file
    """
    core_list = []
    for keyword in keyword_list:
        counter = collections.Counter(generated_dict[keyword])
        for child_key, val in counter.items():
            core_list.append({'key': keyword, 'value': child_key,
                              'count': val})
    return core_list


def get_arguments(args):
    """Function that fetch path from the command line and compute parse_csv
       with user arg which is string parameter

    Args:
        args (str): contains path to csv file (or any char symbols given)

    NOTE:
        The app will stop if the path is incorrect

    Returns:
        parser: parser object which contains result of computing parse_csv
                function
    """
    parser = argparse.ArgumentParser(description='Process file path')
    parser.add_argument('parsed_data',
                        metavar='P',
                        type=parse_csv,
                        help='a string contains absolute path to file')
    return parser.parse_args(args)


if __name__ == '__main__':
    dictionaries, dict_keys = get_arguments(sys.argv[1:]).parsed_data
    parsed_dict, keywords = count_entries(dictionaries, dict_keys)
    logging.info(extending_data_with_keywords(parsed_dict, keywords)[-1::-1])
