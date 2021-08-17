#!/usr/bin/env python3

# how to use a variable inside a string
# the {} {} double brackets hold the variables
# and the f" " formats the string,
# place an f before the "" to insert a vars value into a string

first_name = "peter"
last_name = "gibbons"

full_name = f"{first_name} {last_name}"
print(full_name)

print(60*"-")

city = "tampa"
state = "florida"
country = "united states"
space = "\n\t"

location = f"{space} {state} {country}"
print(location.title())


#--------------------------------------------------------------
print(60*"-")
#print(30*"-"30"_")
#-----------------------------------------------------------------------

# Lists are repped using [] square brackets the 1st item in a list is 0
# list demo:  0                1                2              3
names = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly']
message = f"The funniest character is {names[0].title()}."

#names = print(names[1])
print(message)

#----------------------------------------------------------------------
print(61*"-")
#----------------------------------------------------------------------
#
print(names[0]) #Michael Scott
print(names[2]) #Jim Halpert
print(names[3]) #Pam Beasley
print(names[1]) #Dwight
#
#-----------------------------------------------------------------------
print(60*"-")
#-----------------------------------------------------------------------
print("Function example")

def get_the_office(first, last):

    full = f"{first} {last}"
    return full.title()

while True:
    print("\nWho is your favourite character on The Office?")
    f_first = input("First name: ")
    l_last = input("Last name: ")

    formatted_name = get_the_office(f_first, l_last)
    print(f"\nYour favourite character is {formatted_name}.")
    break

#---------------------------------------------------------------
print(60*"-")
#----------------------------------------------------------------
print(names[0:3]) # prints 0 - 2
#------------------------------------------------------------------

for name in names[:2]:
    print(name.title())

#----------------------------------------------------------------
print(60*"-")
#---------------------------------------------------------------
import time

# While Loop
i = 1

while i > 0:
    time.sleep(0.1)
    i += 1
    print(i)
    if i == 20:
        break

("loop break")

