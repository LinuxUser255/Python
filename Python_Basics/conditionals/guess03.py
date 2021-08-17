#!/usr/bin/env python3

answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

#Round 1
if guess < answer:
     print("Higher, R1")
     guess = int(input())
     if guess == answer:
         print("You got it, R1")
     else:
         print("Sorry, incorrect. R1")
elif guess > answer:
     print("Lower, R1")
     guess = int(input())
     if guess == answer:
         print("You got it, R1")
     else:
        print("Sorry, incorrect. R1")
else:
    print("Congtrats! First try. R1")


#Round 2
if guess < answer:
     print("Higher, R2")
     guess = int(input())
     if guess == answer:
         print("You got it. R2")
     else:
         print("Sorry, incorrect. R2")
elif guess > answer:
     print("Lower. R2")
     guess = int(input())
     if guess == answer:
         print("You got it. R2")
     else:
        print("Sorry, incorrect, R2")
else:
    print("Congrats! First try ,R2")


#Round 3
if guess < answer:
     print("Higher, R3")
     guess = int(input())
     if guess == answer:
         print("You got it. R3")
     else:
         print("Sorry, incorrect. R3")
elif guess > answer:
     print("Lower. R3")
     guess = int(input())
     if guess == answer:
         print("You got it. R3")
     else:
        print("Sorry, incorrect. R3")
else:
    print("Congrats! First try. R3")


#Round 4
if guess < answer:
     print("Higher. R4")
     guess = int(input())
     if guess == answer:
         print("You got it. R4")
     else:
         print("Sorry, incorrect. R4")
elif guess > answer:
     print("Lower. R4")
     guess = int(input())
     if guess == answer:
         print("You got it. R4")
     else:
        print("Sorry, incorrect. R4")
else:
    print("Congrats! First try. ,R4")



