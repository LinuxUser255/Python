#!/usr/bin/env python3

""""
__repr__.py

SYNOPSIS
========
::

    Overview of using the dunder-method __repr__
    
    From the online documentation: https://docs.python.org/3/reference/datamodel.html
    
    Data model
    Objects, values and types

        The object.__repr__(self) is Called by the repr() built-in function to compute the
    “official” string representation of an object. If at all possible, this should look like 
    a valid Python expression that could be used to recreate an object with the same value, 
    (given an appropriate environment). 
    If this is not possible, a string of the form <...some useful description...> 
    should be returned. 
    
        The return value must be a string object. If a class defines
    __repr__() but not __str__(), then __repr__() is also used when an “informal”
    string representation of instances of that class is required.

    This is typically used for debugging, so it is important that the
    representation is information-rich and unambiguous.



DESCRIPTION
===========
Using __repr__

"""

class Car:
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

        def __repr__(self):
            return '__repr__ for Car'

        def __str__(self):
            return '__str__ for Car'


using_bpython_in_the_command_line = """

>>> my_car = Car('red', 30000)
>>> print(my_car)
__str__ for Car
>>> '{}'.format(my_car)
'__str__ for Car'
>>> my_car
__repr__ for Car
>>> repr(my_car)
'__repr__ for Car'

"""

"""
SYNOPSIS
========
::

    Using __repr__ and __add__ to calculate a Polynomial.


    some behaviour to implement --> write some __function_
    top-level function or top-level syntax --> corresponding __

    when adding two obj implement __add__
    when initializing an obj, implement __init__
    when telling python what to do when callinfg on an object, implement __repr__

    x + y -->    __add__
    init x -->   __init__
    repr(x) -->  __repr__

"""

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs


    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)


    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))



p1 = Polynomial(1, 2, 3) # x^2 + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x^2 + 4x + 3
