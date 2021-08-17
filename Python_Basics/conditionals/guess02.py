#!/usr/bin/env python3

# Guessing Game part one with if, else, elif
answer = 50
print("Guess a number between 1 and 50: ")
guess = int(input())

if guess < answer:
    print("Guess higher")
    guess = int(input())
    if guess == 50:
        print("congrats!")
    else:
        print("incorrect")
elif guess > answer:
    print("Guess lower")
    guess = int(input())
    if guess == answer:
        print("correct.")
    else:
        print("Sorry, incorrect")
else:
     print("correct on first try!")
