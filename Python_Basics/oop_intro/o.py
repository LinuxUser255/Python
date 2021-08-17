#!/usr/bin/env python3



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

