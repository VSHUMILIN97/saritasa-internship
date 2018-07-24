# IDEAS:
# Iterate through the whole object (non-effective)
# ???
# Make it like a JSON parse????
import random
names = {'Alex': 0, 'Bob': 0, 'John': 0, 'Cena': 0, 'Doe': 0, 'Michael': 0}
boolean = {'True': 0, 'False': 0}
dicts = []


def build_list():
    # bool(random.getrandbits(1)) May be useful
    for iterable in range(0, 10*10):
        dicts.append({'id': iterable, 'success': random.choice(list(boolean.keys())),
                      'name': random.choice(list(names.keys()))})


def count_enters():
    build_list()
    for each_dict in dicts:
        names.update({each_dict['name']: names[each_dict['name']] + 1})
        boolean.update({each_dict['success']: boolean[each_dict['success']] + 1})


def updating_list():
    count_enters()
    keys = list(dicts[0].keys())[1:]
    dicts.clear()
    success_dict = {'success': boolean}
    names_dict = {'name': names}
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
