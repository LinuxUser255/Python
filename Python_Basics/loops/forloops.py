#!/usr/bin/env python3

import time

print(60*"-")
print("\n")
# The For Loop
# i becomes each variable. Four examples.
#This loop retrieves the values of 0 through 26.
#The last value is not included and thus ends on 25.

# Using the range function --->  range()
# is this one a tuple??
for i in range(0, 26):
    time.sleep(0.1)
    print("this is a range function And i is now {}".format(i))

print("\n")

# and can use the range() with the list()
numbers = list(range(1, 20))
print(numbers)

#-----------------------------------------
print(60*"-")
#----------------------------------------

# Iterate through a range
for i in [1,2,3,4,5,'a','b','c']:
    time.sleep(0.1)
    print(i)


#Use of the replacement field {}. to format and print i.
for i in range(26):
    time.sleep(0.1)
    print("{}".format(i))

#-----------------------------------------
print(60*"-")
#----------------------------------------

for i in range(1,25):
    time.sleep(0.1)
    print("i is now {}".format(i))

print(60*"-")
print("\n")



