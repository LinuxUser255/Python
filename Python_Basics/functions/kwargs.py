#!/usr/bin/env python3

# concatenate.py
def concatenate(**kwargs):
    result = ""

    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
