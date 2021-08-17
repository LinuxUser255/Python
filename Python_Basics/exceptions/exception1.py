#!/usr/bin/env python3

try:          
    f = open('Python_notes.txt')  #incorrect file name
except Exception:
   print("The file you selected does not exist")


#Line 3 is general and can be changed to catch a specific error
