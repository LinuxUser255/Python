#!/usr/bin/env python3
import time

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
# the modulo % is ZERO  (therefore curent_number is divisable by 2)

    time.sleep(0.5)
    print(current_number)
