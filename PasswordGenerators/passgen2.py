#!/usr/bin/env python3
# Password gerator script
# by Chris Bingham
# License: GNU GPLv3
# 1:4 character output in this script. For every one char you input, four are generated.
# Example: If you want a 12 char pw, then enter a pw length of just three characters.

import string
import secrets

length = int(input("Password length: "))

def password_generator(length):
    password = ''  # empty string
    
    for i in range(length):
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
        password += secrets.choice(string.punctuation)
        password += secrets.choice(string.digits)
        

    return password  # returns the string

print(password_generator(length))
