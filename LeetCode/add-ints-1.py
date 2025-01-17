#!/usr/bin/env python3

# This is what I came up with.
# It works on the command line when run as a script, but not in Leet Code
class Solution:
    def __init__(self, num1=12, num2=5):
        self.num2 = None
        self.num1 = None
        self.add(num1, num2)

    def add(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        result = self.num1 + self.num2
        print(result)

if __name__=="__main__":
    Solution().calculate()
