import random
entered_name = {'Alex': 0, 'Bob': 0, 'John': 0, 'Cena': 0, 'Doe': 0, 'Michael': 0}
entered_boolean = {'True': 0, 'False': 0}
list_with_dicts = []


def build_list(f_name, s_name, t_name):
    for enter_iterable in range(0, 10*10):
        list_with_dicts.append({str(f_name): enter_iterable,
                                str(s_name): random.choice(list(entered_boolean.keys())),
                                str(t_name): random.choice(list(entered_name.keys()))
                                })


def count_enters():
    build_list('id', 'Cany', 'Deny')  # TO-DO REFACTOR
    for each_dict in list_with_dicts:
        for appeared_key in each_dict.keys():
            try:
                entered_name.update({each_dict[appeared_key]: entered_name[each_dict[appeared_key]] + 1})
            except KeyError:
                pass
            try:
                entered_boolean.update({each_dict[appeared_key]: entered_boolean[each_dict[appeared_key]] + 1})
            except KeyError:
                pass


def updating_list():
    count_enters()
    current_keys = list(list_with_dicts[0].keys())[1:]
    list_with_dicts.clear()
    link_boolean_dict = {current_keys[0]: entered_boolean}
    link_names_dict = {current_keys[1]: entered_name}
    for every_key in current_keys:
        try:
            appendables = link_boolean_dict[every_key]
        except KeyError:
            appendables = link_names_dict[every_key]
        for every_key in appendables:
            if appendables[every_key] > 1:
                list_with_dicts.append({'key': every_key, 'value': every_key, 'count': appendables[every_key]})


if __name__ == '__main__':
    updating_list()
    print(list_with_dicts)

