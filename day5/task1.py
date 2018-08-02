import copy
from random import shuffle
import sys


class SetLike(object):

    __slots__ = ['unique', 'counter']

    def __init__(self, seq):
        object.__setattr__(self, 'unique', [])
        self.unique = self._set_builder(seq)
        self.do_shuffle()

    @staticmethod
    def _set_builder(seq):
        clear_file = []
        for elem in seq:
            if elem not in clear_file:
                clear_file.append(elem)
        return clear_file

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        if self.counter < self.__len__() - 1:
            self.counter += 1
            return self.unique[self.counter]
        else:
            raise StopIteration()

    def __add__(self, another_set):
        new_object = copy.copy(self.add(another_set))
        return new_object

    def do_shuffle(self, possible_arg=None):
        """ Function which purpose is to mimic the set behaviour.
            Set is not orderly.

        Args:
            possible_arg: Any iterable object that can be shuffled

        Returns:
            object: Shuffled iterable object (Most preferably - list)

        """
        shuffle(self.unique)
        if hasattr(possible_arg, '__iter__'):
            shuffle(possible_arg)
            return possible_arg

    @staticmethod
    def is_instance_fake(other_set):
        """ Function that checks whether instance is set or SetLike object

        Args:
            other_set: user object entry

        Returns:
            bool: True if it is instance of set or SetLike, False otherwise
        """
        if isinstance(other_set, (set, SetLike)):
            return True
        else:
            return False

    def __iadd__(self, other_set):
        self.add(other_set)
        return self.unique

    def add(self, elem, *args, **kwargs):
        """ Add an element to a set.
            This has no effect if the element is already present.
        Args:
            elem (object): Element for the set

        Returns:
            SetLike: Same SetLike with new value (if not present)
        """
        if hasattr(elem, '__iter__'):
            for item in elem:
                if elem in self.unique:
                    pass
                else:
                    self.unique.append(item)
                    self.do_shuffle()
        else:
            self.unique.append(elem)

    def clear(self, *args, **kwargs):
        """ Remove all elements from this set.

        Returns:
            None
        """
        self.unique.clear()

    def copy(self, *args, **kwargs):
        """ Return a shallow copy of a set.

        Returns:
            None
        """
        self.do_shuffle()
        return copy.deepcopy(self.unique)

    def difference(self, elem, *args, **kwargs):
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)

        Args:
            elem (object): Element for the set comparison

        Returns:
            object: New object
        """
        diff = [obj for obj in self.unique if obj not in elem]
        diff = self.do_shuffle(diff)
        return diff

    def difference_update(self, elem, *args, **kwargs):
        """ Remove all elements of another set from this set. """
        update_list = self.difference(elem)
        copied = copy.deepcopy(self.unique)
        self.unique = [val for val in copied
                       if val in update_list and elem not in elem]
        self.do_shuffle()
        return None

    def discard(self, elem, *args, **kwargs):
        """
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        if elem in self.unique:
            self.unique.pop(self.unique.index(elem))

    def intersection(self, elem, *args, **kwargs):
        """
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
        """
        if self.is_instance_fake(elem):
            intersection = [obj for obj in self.unique if obj in elem]
            self.do_shuffle(intersection)
            return intersection

    def intersection_update(self, elem, *args, **kwargs):
        """ Update a set with the intersection of itself and another. """
        for index, val in enumerate(self.unique):
            for subitem in elem:
                if val != subitem:
                    self.unique.pop(index)

    def isdisjoint(self, elem, *args, **kwargs):
        """ Return True if two sets have a null intersection. """
        if not self.intersection(elem):
            return True
        return False

    def issubset(self, elem, *args, **kwargs):
        """ Report whether another set contains this set. """
        if self.is_instance_fake(elem):
            if len(self.unique) >= len(elem):
                return False
            for item in self.unique:
                if item in elem:
                    pass
                else:
                    return False
            return True

    def issuperset(self, elem, *args, **kwargs):  # DONE
        """ Report whether this set contains another set. """
        if self.is_instance_fake(elem):
            for item in elem:
                if item in self.unique:
                    pass
                else:
                    return False
            return True

    def pop(self, elem, *args, **kwargs):  # DONE
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        if not self.unique:
            raise KeyError('No more elements in this beautiful set')
        elif elem in self.unique:
            return self.unique.pop(self.unique.index(elem))

    def remove(self, elem, *args, **kwargs):  # DONE
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        try:
            self.unique.pop(self.unique.index(elem))
        except ValueError:
            raise KeyError('Not in this not like this set')

    def symmetric_difference(self, elem, *args, **kwargs):
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        intersection_res = self.intersection(elem)
        val = [item for item in self.unique if item not in intersection_res]
        val.extend([item for item in elem
                    if item not in intersection_res and
                    item not in val])
        return val

    def symmetric_difference_update(self, elem, *args, **kwargs):
        """ Update a set with the symmetric difference
            of itself and another. """
        self.unique = self.symmetric_difference(elem)
        return self.unique

    def union(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        if self.is_instance_fake(elem):
            union = [obj for obj in self.unique]
            union.extend([obj for obj in elem if obj not in self.unique])
            self.do_shuffle(union)
            return union
        else:
            raise TypeError('Unknown operation for type(s)'
                            f' - SetLike and {type(elem)}')

    def update(self, elem, *args, **kwargs):
        """ Update a set with the union of itself and others. """
        for item in elem:
            if item not in self.unique:
                self.unique.append(item)

    def __and__(self, elem, *args, **kwargs):  # DONE
        return self.intersection(elem)

    def __contains__(self, elem):  # DONE
        """ x.__contains__(y) <==> y in x. """
        if elem in self.unique:
            return True
        else:
            return False

    def __eq__(self, elem, *args, **kwargs):
        """ Return self==value. """
        if self.is_instance_fake(elem):
            if elem == self.unique:
                return True
            else:
                return False

    def __ge__(self, elem, *args, **kwargs):
        """ Return self>=value. """
        return self.issuperset(elem)

    def __getattr__(self, item):
        return item

    def __gt__(self, elem, *args, **kwargs):
        """ Return self>value. """
        if self.is_instance_fake(elem):
            for item in elem:
                if item in self.unique:
                    pass
                else:
                    return False
            if len(elem) == len(self.unique):
                return False
            return True

    def __iand__(self, elem, *args, **kwargs):  # DONE
        """ Return self&=value. """
        self.unique = self.intersection(elem)
        return self.unique

    def __ior__(self, elem, *args, **kwargs):  # DONE
        """ Return self|=value. """
        self.unique = self.union(elem)
        return self.union(elem)

    def __isub__(self, elem, *args, **kwargs):  # DONE
        """ Return self-=value. """
        self.difference_update(elem)
        return self.unique

    def __ixor__(self, elem, *args, **kwargs):  # DONE
        """ Return self^=value. """
        return self.symmetric_difference_update(elem)

    def __len__(self, *args, **kwargs):  # DONE
        """ Return len(self). """
        return len(self.unique)

    def __le__(self, elem, *args, **kwargs):  # DONE
        """ Return self<=value. """
        if self.is_instance_fake(elem):
            for item in self.unique:
                if item in elem:
                    pass
                else:
                    return False
            if len(elem) == len(self.unique):
                return False
            return True

    def __lt__(self, elem, *args, **kwargs):  # DONE
        """ Return self<value. """
        return self.issubset(elem)

    def __ne__(self, elem, *args, **kwargs):  # DONE
        """ Return self!=value. """
        return self.isdisjoint(elem)

    def __or__(self, elem, *args, **kwargs):  # DONE
        """ Return self|value. """
        return self.union(elem)

    def __rand__(self, elem, *args, **kwargs):  # DONE
        """ Return value&self. """
        return SetLike(elem).intersection(self.unique)

    def __reduce__(self, *args, **kwargs):
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        return self.unique

    def __ror__(self, elem, *args, **kwargs):
        """ Return value|self. """
        return SetLike(elem).union(self.unique)

    def __rsub__(self, elem, *args, **kwargs):
        """ Return value-self. """
        return SetLike(elem).__sub__(self.unique)

    def __rxor__(self, elem, *args, **kwargs):
        """ Return value^self. """
        return SetLike(elem).symmetric_difference(self.unique)

    def __sizeof__(self):
        """ S.__sizeof__() -> size of S in memory, in bytes """
        return sys.getsizeof(self.unique)

    def __sub__(self, elem, *args, **kwargs):
        """ Return self-value. """
        self.difference_update(elem)
        return self.unique

    def __xor__(self, elem, *args, **kwargs):
        """ Return self^value. """
        return self.symmetric_difference(elem)

    def __str__(self):
        self.do_shuffle()
        return str(self.unique)

    __hash__ = None
