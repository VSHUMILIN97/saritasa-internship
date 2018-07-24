

sequence = {'A': 'А', 'B': 'Б', 'C': 'К',
            'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х',
            'I': 'И', 'J': 'Ж', 'K': 'К', 'L': 'Л', 'M': 'М',
            'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'КЬ', 'R': 'Р',
            'S': 'C', 'T': 'Т', 'U': 'У', 'V': 'B', 'W': 'ВЬ',
            'X': 'КС', 'Y': 'У', 'Z': 'З'}

reversed_sequence = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
                     'Ё': 'YO', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'YI', 'К': 'K',
                     'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
                     'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ч': 'CH',
                     'Ц': 'CE', 'Ш': 'SH', 'Щ': 'SH', 'Э': 'E', 'Ю': 'UY', 'Я': 'YA',
                     'Ь': '', 'Ъ': '', 'Ы': 'II'}


def translite():
    try:
        string = input('Введите строку на английском или русском языке: ')
    except IOError:
        string = 'Стандартная строка для перевода'

    example = ''
    for item in string:
        try:
            example += sequence[item.upper()]
        except KeyError:
            try:
                example += reversed_sequence[item.upper()]
            except KeyError:
                exit(0)

    return example


# if __name__ == 'main':
    # print(translite())
print(translite())
