#!/usr/bin/env python3

# Goal:
# Easily update the Employee's Name.
# Solution:
# Use the @property decorator
# The Property Decorator: easy method definition & access as if it were an attribute
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self): # descriptor
        email = f"{self.first}.{self.last}@email.com"
        return email

    @property
    def fullname(self):
        fullname = f"{self.first} {self.last}"
        return fullname.title()

    @fullname.setter
    def fullname(self, name):
    '''Defines the fullname of the Employee class'''
        first, last = name.split(' ')
        self.first = first
        self.last = last


# Employee Object
emp_1 = Employee('the', 'dude')
emp_1.fullname = 'jim smith'

# print the employee's name
print(f"{emp_1.first}\n{emp_1.email}\n{emp_1.fullname}")

