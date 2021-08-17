#!/usr/bin/env python3

# Error handling with a while loop
# Use the else block to increase error resistance

print("enter 2 numbers to divide")
print("enter q to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Not able to divide by zero")
    else:
        print(answer)

