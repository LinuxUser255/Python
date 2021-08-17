#!/usr/bin/env python3

#Passing an argument to a function.
def get_formatted_car(make, model):
    full = f"{make} {model}"
    return full.title()


#While loop
while True:
    print ("\nWhat is the make and model of your car? ")
    f_make = input("Make: ")
    s_model = input("Model: ")

    formatted_car = get_formatted_car(f_make, s_model)
    print(f"\nYou drive a {formatted_car}. Nice.")
    break


# Toyota Corolla
