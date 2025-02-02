#!/usr/bin/env python3

import time

def sum_even_numbers(numbers):
    start_time = time.time()
    result = sum(num for num in numbers if not num & 1)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.20f} seconds")
    return result
