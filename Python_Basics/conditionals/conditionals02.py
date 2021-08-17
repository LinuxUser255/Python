#!/usr/bin/env python3

# Guessing Game with if, else, elif

print("Guess a number between 1 and 50: ")
guess = int(input())

if guess < 50:
    print("Guess higher")
    guess = int(input())
    if guess == 50:
        print("congrats!")
    else:
        print("try again")
elif guess > 50:
    print("Guess lower")
    guess = int(input())
    if guess == 50:
        print("congrats! that is correct.")
    else:
        print("try again")
else:
     print("first try correct")
