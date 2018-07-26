"""Simple script which purpose is to generate csv
   with random keys and values"""
from faker import Faker
import logging
import csv


if __name__ == '__main__':
    fake = Faker()
    try:
        with open('data.csv', 'w') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for x in range(100 * 100):
                writer.writerow({'id': x, 'name': fake.name(),
                                 'age': fake.random.randint(14, 50)})
    except IOError:
        logging.error('Cannot reach the file')
        exit(0)
