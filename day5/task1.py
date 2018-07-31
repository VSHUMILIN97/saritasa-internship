class SetLike:

    def __init__(self, obj):
        self.unique = []
        try:
            self.unique += [x for x in iter(obj)]
        except TypeError:
            self.unique += obj

    def __iter__(self):
        return self

    def __next__(self):
        counter, start = len(self.unique), -1
        if start < counter:
            start += 1
            return start
        else:
            raise StopIteration()

    def __add__(self, another_set):
        try:
            for x in another_set:
                if x not in self.unique:
                    self.unique.append(x)
            new_object = self.unique
            return new_object
        except TypeError:
            print('BlepBlopMistake')
            exit(1)

    def __iadd__(self, other_set):
        try:
            for x in other_set:
                if x not in self.unique:
                    self.unique.append(x)
            return self.unique
        except TypeError:
            print('BlepMistake')
            exit(1)

    def add(self, elem, *args, **kwargs):  # real signature unknown
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        if elem in self.unique:
            pass
        else:
            self.unique.append(elem)

    def clear(self, *args, **kwargs):  # real signature unknown
        """ Remove all elements from this set. """
        self.unique.clear()

    def copy(self, *args, **kwargs):  # real signature unknown
        """ Return a shallow copy of a set. """
        return self.unique.copy()

    def difference(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        diff = []
        for x in self.unique:
            diff.append(x)
        for x in elem:
            if x not in diff:
                diff.append(x)
        return diff

    def difference_update(self, diff, *args, **kwargs):  # real signature unknown
        """ Remove all elements of another set from this set. """
        for x, _ in enumerate(self.unique):
            if self.unique[x] in diff:
                self.unique.pop(x)

    def discard(self, elem, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        if elem in self.unique:
            self.unique.pop(self.unique.index(elem))

    def intersection(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
        """
        intersection = []
        for x in self.unique:
            for y in elem:
                if x == y:
                    intersection.append(x)
        return intersection

    def intersection_update(self, elem, *args, **kwargs):  # real signature unknown
        """ Update a set with the intersection of itself and another. """
        for x, val in enumerate(self.unique):
            for y in elem:
                if val != y:
                    self.unique.pop(x)

    def isdisjoint(self, elem, *args, **kwargs):  # real signature unknown
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

    def issubset(self, elem, *args, **kwargs):  # real signature unknown
        """ Report whether another set contains this set. """
        for x in self.unique:
            if x in elem:
                continue
            else:
                return False
        return True

    def issuperset(self, elem, *args, **kwargs):  # real signature unknown
        """ Report whether this set contains another set. """
        self.__contains__(elem)

    def pop(self, elem, *args, **kwargs):  # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        if not self.unique:
            raise KeyError('No more elements in this beautiful set')
        elif elem in self.unique:
            return self.unique.pop(self.unique.index(elem))

    def remove(self, value, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        try:
            self.unique.pop(value)
        except ValueError:
            raise KeyError('Not in this not like this set')

    def symmetric_difference(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        intersection = []
        for x in self.unique:
            for y in elem:
                if x != y:
                    intersection.append(x)
        for x in elem:
            if x not in intersection:
                intersection.append(x)
        return intersection

    def symmetric_difference_update(self, elem, *args, **kwargs):  # real signature unknown
        """ Update a set with the symmetric difference of itself and another. """
        for x in self.unique:
            for y in elem:
                if x != y:
                    self.unique.append(y)
        for x in elem:
            if x not in self.unique:
                self.unique.append(x)

    def union(self, elem, *args, **kwargs):  # real signature unknown
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        union = []
        for x in self.unique:
            for y in union:
                if y not in union:
                    union.append(y)
                if x not in union:
                    union.append(x)
        return union

    def update(self, elem, *args, **kwargs):  # real signature unknown
        """ Update a set with the union of itself and others. """
        for y in elem:
            if y not in self.unique:
                self.unique.append(y)

    def __and__(self, *args, **kwargs):  # real signature unknown
        """ Return self&value. """
        pass

    def __contains__(self, y):  # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x. """
        for x in y:
            if x in self.unique:
                continue
            else:
                return False
        return True

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        return self.unique

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __iand__(self, *args, **kwargs):  # real signature unknown
        """ Return self&=value. """
        pass

    def __ior__(self, *args, **kwargs):  # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs):  # real signature unknown
        """ Return self-=value. """
        pass

    def __ixor__(self, *args, **kwargs):  # real signature unknown
        """ Return self^=value. """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs):  # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs):  # real signature unknown
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Return state information for pickling. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        return self.unique

    def __ror__(self, *args, **kwargs):  # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs):  # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs):  # real signature unknown
        """ Return value^self. """
        pass

    def __sizeof__(self):  # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __sub__(self, *args, **kwargs):  # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs):  # real signature unknown
        """ Return self^value. """
        pass

    __hash__ = None
