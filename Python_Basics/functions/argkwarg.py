#!/usr/bin/env python3

def argkwarg(a, b, *args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
argkwarg('Python','for','OOP',first="Python",mid="for",last="OOP")
