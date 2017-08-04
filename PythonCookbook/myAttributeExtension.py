

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('Cannot delete attribute')


class SubPersion(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPersion, SubPersion).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPersion, SubPersion).name.__delete__(self)


s = SubPersion('Guido')
s.name
s.name = 'Larry'
p = Person('Bob')
p.name
print(s.__dict__)