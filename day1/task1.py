"""
"""
import csv
import logging
import argparse


def parse_csv(path_to_file):
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
    output_list = []
    output_dict = {}
    for each_dict in generated_list:
        for key, val in each_dict.items():
            output_dict.setdefault('key', key)
            output_dict.setdefault('value', val)
            output_dict.setdefault('count', 0)
            output_list.append(output_dict)
    for every_dict in output_list:
        for same_dict in output_list:
            if every_dict is same_dict:
                every_dict['count'] += 1
    return output_list


def get_arguments():
    parser = argparse.ArgumentParser(description='Process file path')
    parser.add_argument('path', metavar='P', type=str,
                        help='a string contains absolute path to file')
    return parser.parse_args()


if __name__ == '__main__':
    parse_result = parse_csv(get_arguments())
    print(count_entries(parse_result[0], parse_result[1]))

