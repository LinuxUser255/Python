#!/usr/bin/env python3
# Password Generator Script
# by Chris Bingham
# License: GNU GPLv3
#Generate a random password of any desired length and any desired number of passwords.
import random 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!@#$%&-_=+?!@#$%&-_=+?'
length = int(input("Number length: "))
number = int(input("Number of random numbers: "))


def generate_number() -> str:
    for n in range(number):
        pass_list = ''
        for i in range(length):
          pass_list += random.choice(chars)
        print(pass_list)


if __name__=="__main__":
    generate_number()
