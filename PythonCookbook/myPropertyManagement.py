class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # dEleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p = Person("1")
print(p.first_name)


class Fee(object):
    """"""
    def __init__(self):
        """Constructor"""
        self._fee = None

    @property
    def fee(self):
        """
         The fee property - the getter
        """
        return self._fee

    @fee.setter
    def fee(self, value):
        if isinstance(value, str):
            self._fee = int(value)
        elif isinstance(value, int):
            self._fee = value

f = Fee()
f.fee = 12
print(f.fee)

from decimal import Decimal
########################################################################
class Fees(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None

    #----------------------------------------------------------------------
    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee

    #----------------------------------------------------------------------
    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)