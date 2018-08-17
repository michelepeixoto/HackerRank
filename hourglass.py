#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = 0
    sum_lst = []
    max_sum = -999999999
    max_pos = 0, 0
    
    for x in range(4):
        outter = 0
        inner = 1
        for y in range(4):
            sum_lst = arr[x][outter:outter+3]
            sum_lst.append(arr[x+1][inner]) 
            sum_lst.extend(arr[x+2][outter:outter+3])
            for num in sum_lst:
                sum += num
            if sum > max_sum:
                max_sum = sum
                max_pos = x, y
            outter += 1
            inner += 1
            
    hourglass = ''
    for num in arr[max_pos[0]][max_pos[1]:max_pos[1]+3]:
        hourglass += str(num)
    hourglass += '\n'
    hourglass += str(arr[max_pos[0]+1][max_pos[1]+1])
    hourglass += '\n'
    for num in arr[max_pos[0]+2][max_pos[1]:max_pos[1]+3]:
        hourglass += str(num)
    return hourglass
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
