"""This script provide a function
   that translates russian text to transliteration and vice versa.
   Ex:
        “Эта строка будет подвержена транслитерации” ->
        “Eta stroka budet podverzhena tranliteracii”
"""
import os
SEQUENCE_TASK_0 = \
        {'A': 'А',
            'B': 'Б',
            'C': 'К',
            'D': 'Д',
            'E': 'Е',
            'F': 'Ф',
            'G': 'Г',
            'H': 'Х',
            'I': 'И',
            'J': 'Ж',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'Q': 'КЬ',
            'R': 'Р',
            'S': 'C',
            'T': 'Т',
            'U': 'У',
            'V': 'В',
            'W': 'ВЬ',
            'X': 'КС',
            'Y': 'У',
            'Z': 'З',
            'А': 'A',
            'Б': 'B',
            'В': 'V',
            'Г': 'G',
            'Д': 'D',
            'Е': 'E',
            'Ё': 'YO',
            'Ж': 'J',
            'З': 'Z',
            'И': 'I',
            'Й': 'YI',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'Ф': 'F',
            'Х': 'H',
            'Ч': 'CH',
            'Ц': 'CE',
            'Ш': 'SH',
            'Щ': 'SH',
            'Э': 'E',
            'Ю': 'UY',
            'Я': 'YA',
            'Ь': '',
            'Ъ': '',
            'Ы': 'II'}


def setup_user_environment():
    """Function that collects current language
       settings from the user's environment

    Returns:
        string: value that contains current language settings
    """
    try:
        user_language = os.getenv('LANG')
    except OSError:
        user_language = 'ru'
    return user_language


def get_string_from_user(current_language):
    """Function which purpose is to collect prompt from user

    Args:
        current_language (str): receiver of language settings

    Returns:
        string: value that contains user prompt for the transliteration
    """
    if current_language.startswith('ru'):
        user_prompt = input('Введите строку на английском или русском языке: ')
    else:
        user_prompt = input('Enter a prompt in English or Russian: ')
    return user_prompt


def transliteration():
    """Function that transliterate from eng to rus and vice versa.

    NOTE:
        There is a global dictionary that contains prepared data.

    Returns:
        string: prompt to output
    """

    output_string = ''
    for each_char in get_string_from_user(setup_user_environment()):
        if each_char.upper() in SEQUENCE_TASK_0.keys():
            output_string += SEQUENCE_TASK_0[each_char.upper()].lower() \
                if each_char.islower()\
                else SEQUENCE_TASK_0[each_char.upper()].upper()
        else:
            output_string += each_char
    return output_string


if __name__ == '__main__':
    print(transliteration())
