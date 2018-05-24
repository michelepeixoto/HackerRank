#!/bin/python3

import os
import sys

# takes in an integer n denoting the number of lines of the program and returns the maximum value. 
# You will need to take the program's lines from the standard input.
def maximumProgramValue(n):
    x = 0
    for i in range(n):
        action = input()
        num = int(action[3:].strip())
        if action[:3] == "add":
            if num > 0:
                x += num
            pass
        elif action[:3] == "set":
            if num > x:
                x = num
            pass
    return x

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = maximumProgramValue(n)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
