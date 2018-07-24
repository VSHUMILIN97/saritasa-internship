# IDEAS:
# Iterate through the whole object (non-effective)

import random
names = {'Alex': 0, 'Bob': 0, 'John': 0, 'Cena': 0, 'Doe': 0, 'Michael': 0}
boolean = {'True': 0, 'False': 0}
dicts = []


def build_list(fname, sname, tname):
    for iterable in range(0, 10*10):
        dicts.append({str(fname): iterable, str(sname): random.choice(list(boolean.keys())),
                      str(tname): random.choice(list(names.keys()))})


def count_enters():
    build_list('id', 'any', 'many')
    for each_dict in dicts:
        for key in each_dict.keys():
            try:
                names.update({each_dict[key]: names[each_dict[key]] + 1})
            except KeyError:
                pass
            try:
                boolean.update({each_dict[key]: boolean[each_dict[key]] + 1})
            except KeyError:
                pass


def updating_list():
    count_enters()
    keys = list(dicts[0].keys())[1:]
    dicts.clear()
    success_dict = {keys[0]: boolean}
    names_dict = {keys[1]: names}
    for rec in keys:
        try:
            appendables = success_dict[rec]
        except KeyError:
            appendables = names_dict[rec]
        for every_key in appendables:
            if appendables[every_key] > 1:
                dicts.append({'key': rec, 'value': every_key, 'count': appendables[every_key]})


updating_list()
print(dicts)

