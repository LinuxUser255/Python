#!/usr/bin/env python3

try:         
    f = open('Python_Notes.txt')
except FileNotFoundError as v:
    print(v)
except Exception as v:
    print(v)
else:
    print(f.read())
    f.close()
finally:
    print("Execution Complete. Resources closed.")
