from pprint import pprint
import copy

"""
TO-DO:
    * Fix that Attribute error (__getattr__)
    * Implement possibility to restrict_items
    * Write tests
"""


def setup_dict_factory(dictionary, add=False, change=False, delete=False):
    return ReadOnlyDict(dictionary, add, change, delete)


class ReadOnlyDict(object):
    """ This class initialise a ReadOnly dictionary which
        purpose is to make dicts much more flexible in
        customization and ease accessing to their attributes

    Examples:
        For object = {'inc':
                         {'monster':
                             {'Sally': 'Bear', 'Michael': 'Green Ball'}
                         }
        } you can access value Green Ball like:
        ReadOnlyDict(object).inc.monster.Michael
        The example above will return you 'Green Ball'
        Also you can extend this object easily:
        object.inc.monster.Simon = 'Lizard'

    Note:
        The example above will return you None. All changes are in-place

    Attributes:
        dict (dict): User dictionary to work with
        add (bool): Add property
        change (bool): Change property
        delete (bool): Delete property
        *args (list): Additional positional args
        **kwargs (dict): Additional keyword args
    """
    def _set_initials(self, name, value):
        """ This function remove redundancy while creating
            an object at __init__

        Args:
            name (str): namespace in this class
            value (obj): value of this namespace

        Returns:
            object: prepared base object with __setattr__
        """
        return object.__setattr__(self, name, value)

    def __init__(self,
                 dict,
                 add=False,
                 change=False,
                 delete=False,
                 *args,
                 **kwargs):
        self._set_initials('user_dict', dict)
        self._set_initials('add', add)
        self._set_initials('change', change)
        self._set_initials('delete', delete)

    def __setattr__(self, key, value):
        if self.add:
            self.user_dict[key] = value
        elif self.change:
            if not self.add:
                raise ValueError('Not permitted to add stuff')
            else:
                self.user_dict[key] = value

    def get_sibling(self, item):
        """ Function that returns 'leaf' value

        Args:
            item (immutable): Key of the dictionary

        Returns:
            ReadOnlyDict: If there are nested dicts inside
            object: Value that stores in the 'leaf' of the dict
        """
        if isinstance(self.user_dict[item], dict):
            sibling = ReadOnlyDict(self.user_dict[item],
                                   self.add, self.change, self.delete)
            return sibling
        else:
            return self.user_dict[item]

    def __getattr__(self, item):
        if self.user_dict.get(item) is None:
            raise ValueError('Unknown attribute')
        else:
            return self.get_sibling(item)

    def __delattr__(self, item):
        if self.delete:
            self.user_dict.pop(item)
        else:
            raise AttributeError('Not permitted to delete')

    def dig_nested_dict(self, data):
        """ Construct nested ReadOnlyDicts
            from nested dictionaries. """
        if not isinstance(data, dict):
            return data
        else:
            return ReadOnlyDict({
                key: ReadOnlyDict.dig_nested_dict(self, data[key])
                for key in data})


if __name__ == '__main__':
    dd = {'name': 'Tor', 'info': {'age': 10, 'secret': 12}}
    d2d = copy.deepcopy(dd)
    a = ReadOnlyDict(dd)
    pprint(f'Getting a.info.age - {a.info.age}')
    pprint(f'Getting a.name - {a.name}')
    b = setup_dict_factory(d2d, add=True, change=True, delete=True)
    print(f'"b" object dict before inserting - {b.user_dict}')
    b.info.future = 'KOI-8'
    b.info.age = 'kek'
    del b.name
    print(f'Full "a" object dict after reading - {a.user_dict}')
    print(f'Full "b" object dict after inserting - {b.user_dict}')
