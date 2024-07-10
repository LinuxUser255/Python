#!/usr/bin/env python3

#Casear cipher
#mv ech char fwd by 3
#Plain txt ABCDEFG...
#Cipher txt DEFGHI...

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("message:  ")
 

n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    print( i, c, loc, end=" ")
    newloc = loc + 3
    str_out += alpha[newloc]
    print(newloc, str_out)

print("Obsfuscated version: ", str_out)
