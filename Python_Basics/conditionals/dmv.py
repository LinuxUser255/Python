#!/usr/bin/env python3

#If-else using user defined input:
print("""Legal driving age.
        """)

age = int(input("What is your age? "))

if age < 16:
    print("No.")
else:
    if age in range(16, 67):
        print("Yes, you are eligible.")
if age > 66:
    print("Yes, but with special requirements.")
