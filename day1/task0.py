import os
sequence = {'A': 'А', 'B': 'Б', 'C': 'К',
            'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х',
            'I': 'И', 'J': 'Ж', 'K': 'К', 'L': 'Л', 'M': 'М',
            'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'КЬ', 'R': 'Р',
            'S': 'C', 'T': 'Т', 'U': 'У', 'V': 'В', 'W': 'ВЬ',
            'X': 'КС', 'Y': 'У', 'Z': 'З'}

reversed_sequence = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
                     'Ё': 'YO', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'YI', 'К': 'K',
                     'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
                     'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ч': 'CH',
                     'Ц': 'CE', 'Ш': 'SH', 'Щ': 'SH', 'Э': 'E', 'Ю': 'UY', 'Я': 'YA',
                     'Ь': '', 'Ъ': '', 'Ы': 'II'}


def transliteration():
    try:
        get_language = os.getenv('LANG')
    except OSError:
        get_language = 'ru'
    if get_language.startswith('ru'):
        try:
            input_from_user = input('Введите строку на английском или русском языке: ')
        except IOError:
            input_from_user = 'Стандартная строка для перевода'
    else:
        try:
            input_from_user = input('Enter a prompt in English or Russian: ')
        except IOError:
            input_from_user = 'Default prompt for the translation'
    #
    output_sring = ''
    for each_char in input_from_user:
        try:
            rus_char = sequence[each_char.upper()]
            if each_char.islower():
                output_sring += rus_char.lower()
            else:
                output_sring += rus_char
        except KeyError:
            try:
                eng_char = reversed_sequence[each_char.upper()]
                if each_char.islower():
                    output_sring += eng_char.lower()
                else:
                    output_sring += eng_char
            except KeyError:
                output_sring += each_char
    return output_sring


if __name__ == '__main__':
    print(transliteration())

