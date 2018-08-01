import copy
from random import shuffle
import sys


class SetLike(object):

    def __init__(self, seq):
        self.unique = []
        self.zero = -1
        for x in seq:
            if x not in self.unique:
                self.unique.append(x)
        self.do_shuffle()

    def __iter__(self):
        return self

    def __next__(self):
        if self.zero < self.__len__() - 1:
            self.zero += 1
            return self.unique[self.zero]
        else:
            self.zero = -1
            raise StopIteration()

    def __add__(self, another_set):
        if self.is_instance_fake(another_set):
            new_object = copy.deepcopy(self.unique)
            new_object.extend([x for x in another_set if x not in new_object])
            return new_object
        else:
            raise TypeError('Unknown opperand for type(s)'
                            f' - SetLike and {type(another_set)}')

    def do_shuffle(self, possible_arg=None):
        shuffle(self.unique)
        if hasattr(possible_arg, '__iter__'):
            shuffle(possible_arg)
            return possible_arg

    @staticmethod
    def is_instance_fake(other_set):
        if isinstance(other_set, (set, SetLike)):
            return True
        else:
            return False

    def __iadd__(self, other_set):
        if self.is_instance_fake(other_set):
            self.unique.extend([x for x in other_set if x not in self.unique])
            self.do_shuffle()
            return SetLike(self.unique)
        else:
            raise TypeError('Unknown opperand for type(s)'
                            f' - SetLike and {type(other_set)}')

    def add(self, elem, *args, **kwargs):
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        if elem in self.unique:
            pass
        else:
            self.unique.append(elem)
            self.do_shuffle()

    def clear(self, *args, **kwargs):
        """ Remove all elements from this set. """
        self.unique.clear()

    def copy(self, *args, **kwargs):
        """ Return a shallow copy of a set. """
        self.do_shuffle()
        return self.unique.copy()

    def difference(self, elem, *args, **kwargs):
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        diff = [x for x in self.unique if x not in elem]
        diff = self.do_shuffle(diff)
        return diff

    def difference_update(self, diff, *args, **kwargs):
        """ Remove all elements of another set from this set. """
        self.__sub__(diff)

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
        return self.__and__(elem)

    def intersection_update(self, elem, *args, **kwargs):
        """ Update a set with the intersection of itself and another. """
        for x, val in enumerate(self.unique):
            for y in elem:
                if val != y:
                    self.unique.pop(x)

    def isdisjoint(self, elem, *args, **kwargs):
        """ Return True if two sets have a null intersection. """
        intersection = []
        for x in self.unique:
            for y in elem:
                if x == y:
                    intersection.append(x)
        if not intersection:
            return True
        else:
            return False

    def issubset(self, elem, *args, **kwargs):
        """ Report whether another set contains this set. """
        self.__ge__(elem)

    def issuperset(self, elem, *args, **kwargs):
        """ Report whether this set contains another set. """
        self.__contains__(elem)

    def pop(self, elem, *args, **kwargs):
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        if not self.unique:
            raise KeyError('No more elements in this beautiful set')
        elif elem in self.unique:
            return SetLike(self.unique.pop(self.unique.index(elem)))

    def remove(self, value, *args, **kwargs):
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        try:
            self.unique.pop(value)
        except ValueError:
            raise KeyError('Not in this not like this set')

    def symmetric_difference(self, elem, *args, **kwargs):
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        intersection = [x for x in self.unique if x not in elem]
        intersection.extend([x for x in elem if x not in intersection])
        intersection = self.do_shuffle(intersection)
        return intersection

    def symmetric_difference_update(self, elem, *args, **kwargs):
        """ Update a set with the symmetric difference
            of itself and another. """
        self.__xor__(elem)

    def union(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        return self.__or__(elem)

    def update(self, elem, *args, **kwargs):
        """ Update a set with the union of itself and others. """
        for y in elem:
            if y not in self.unique:
                self.unique.append(y)

    def __and__(self, key, *args, **kwargs):  # real signature unknown
        if self.is_instance_fake(key):
            intersection = [x for x in self.unique if x in key]
            self.do_shuffle(intersection)
            return intersection

    def __contains__(self, y):  # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x. """
        if y in self.unique:
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
        if self.is_instance_fake(elem):
            for item in elem:
                if item in self.unique:
                    pass
                else:
                    return False
            return True

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

    def __iand__(self, elem, *args, **kwargs):
        """ Return self&=value. """
        if self.is_instance_fake(elem):
            intersection = [x for x in self.unique if x in elem]
            self.unique = copy.deepcopy(intersection)
            self.do_shuffle()
            return self.unique

    def __ior__(self, elem, *args, **kwargs):
        """ Return self|=value. """
        if self.is_instance_fake(elem):
            union = [x for x in self.unique]
            union.extend([y for y in elem if y not in self.unique])
            self.unique = copy.deepcopy(union)
            self.do_shuffle()
            return self.unique
        else:
            raise TypeError('Unknown operation for type(s)'
                            f' - SetLike and {type(elem)}')

    def __isub__(self, elem, *args, **kwargs):
        """ Return self-=value. """
        if self.is_instance_fake(elem):
            for every_val in elem:
                if every_val in self.unique:
                    self.unique.pop(self.unique.index(every_val))
            self.do_shuffle()
            return self.unique

    def __ixor__(self, elem, *args, **kwargs):
        """ Return self^=value. """
        priv = self.__and__(elem)
        for item in elem:
            if item not in priv:
                self.unique.append(item)
        self.do_shuffle()
        return self.unique

    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        return len(self.unique)

    def __le__(self, elem, *args, **kwargs):
        """ Return self<=value. """
        if self.is_instance_fake(elem):
            for item in self.unique:
                if item in elem:
                    pass
                else:
                    return False
            return True

    def __lt__(self, elem, *args, **kwargs):
        """ Return self<value. """
        if self.is_instance_fake(elem):
            for item in self.unique:
                if item in elem:
                    pass
                else:
                    return False
            if len(elem) == len(self.unique):
                return False
            return True

    def __ne__(self, elem, *args, **kwargs):
        """ Return self!=value. """
        if self.is_instance_fake(elem):
            for item in self.unique:
                if item in elem:
                    pass
                else:
                    return True
            return False

    def __or__(self, elem, *args, **kwargs):
        """ Return self|value. """
        if self.is_instance_fake(elem):
            union = [x for x in self.unique]
            union.extend([y for y in elem if y not in self.unique])
            self.do_shuffle(union)
            return union
        else:
            raise TypeError('Unknown operation for type(s)'
                            f' - SetLike and {type(elem)}')

    def __rand__(self, *args, **kwargs):
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs):
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        return self.unique

    def __ror__(self, *args, **kwargs):
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs):
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs):
        """ Return value^self. """
        pass

    def __sizeof__(self):
        """ S.__sizeof__() -> size of S in memory, in bytes """
        return sys.getsizeof(self.unique)

    def __sub__(self, elem, *args, **kwargs):
        """ Return self-value. """
        if self.is_instance_fake(elem):
            d_copy = copy.deepcopy(self.unique)
            for every_val in elem:
                if every_val in d_copy:
                    d_copy.pop(d_copy.index(every_val))
            self.do_shuffle(d_copy)
            return d_copy

    def __xor__(self, elem, *args, **kwargs):
        """ Return self^value. """
        if self.is_instance_fake(elem):
            priv = self.__and__(elem)
            d_copy = copy.deepcopy(self.unique)
            for item in elem:
                if item not in priv:
                    d_copy.append(item)
            self.do_shuffle(d_copy)
            return d_copy

    def __str__(self):
        self.do_shuffle()
        return str(self.unique)

    __hash__ = None


a = SetLike([1, 2, 3, 3, 15, 22, 22])
a += {11}
b = SetLike([2, 4, 6, 10])
a.add(12)
b.add(12)
b.add(3)

print(a.intersection(b), a.__and__(b))
print(a | b, a.union(b))
print(a - b, a.difference(b))
a.add(10)
b.add(1)
print(a, b)
print(a ^ b, a.symmetric_difference(b))
print(a >= b)
print(a > b)
print(a != b)
print(a < b)
print(a == b)
a &= b
print(a)
a += b
print(a)
a |= b
print(a)
a ^= b
print(a)
