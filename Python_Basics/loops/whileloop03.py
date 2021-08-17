#!/usr/bin/env python3

import time

# While loop with break example
# while a condition is true, do..
i = 0

while(True):
        i += 1
        time.sleep(0.05)
        if (i == 60):
            print("Reached 60")
            time.sleep(1.0)
            continue
        print(i)
        if (i == 80):
            break


#Combine continue with break for more control.


