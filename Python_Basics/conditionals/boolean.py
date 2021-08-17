#!/usr/bin/env python3

#Truth Value Testing
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)


if 0:
    print("True")
else:
    print("False")

OS = input("What Operating System are you using? ")
if OS != "":
     print("How long you been runnin' " + str(OS) + "?")
     
else:
    print("What? You dont use computers?")

