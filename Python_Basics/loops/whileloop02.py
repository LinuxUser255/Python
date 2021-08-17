#!/usr/bin/env python3

import time, struct, sys
# While loops example 1

i=["0"]

max_n = 201

counter = 10

increment = 10

while len(i) <= max_n:
    i.append("i"*counter)
    counter=counter+increment 
    print("{}".format(i))
