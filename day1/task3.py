"""This script validate template strings.

Example of contents on which will basis the string structure:
    {
        'id': 1,
        'name': 'Alice',
        'action': 'Attack Bob'
    }

It provides users with errors that will describe the problem in template.

"""
import logging
from faker import Faker
from string import Template


def build_string(structure, user_prompt):
    """This function builds a string based on user template.
    If template doesn't fit to the current structure
    error will be raised.

    Args:
        structure (dict): provides Template structure
        user_prompt (str): provides text for Template Builder

    Returns:
        String: Prepared string from the users template
        SystemExit: Code 1 in case of any mistake
    """
    example = Template(user_prompt.replace('{', '${'))
    try:
        prepared_string = example.substitute(name=structure['name'],
                                             age=structure['age'],
                                             workplace=structure['workplace'],
                                             quote=structure['quote'],
                                             marriage=structure['marriage'])
        return prepared_string
    except KeyError as e:
        logging.error(f'Incorrect field → {e}')
        return exit(1)
    except ValueError as e:
        logging.error(e)
        return exit(1)


if __name__ == '__main__':
    fake_object = Faker()
    print(build_string({
        'name': fake_object.name(),
        'age': int(18 + fake_object.random.random()*10),
        'workplace': fake_object.address(),
        'quote': fake_object.text(),
        'marriage': True,
    }, input('Please proceed with the string format: ')))
