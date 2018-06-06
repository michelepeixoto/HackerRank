#!/bin/python3

import os
import sys
from decimal import *

# Takes in an integer array  denoting the ratings of the employees and prints the average rating of employees who will get a bonus, with exactly 2 digits after the decimal point, rounded half up
def averageOfTopEmployees(rating):
    topPerformers = []
    average = 0.0
    for score in rating:
        if score >= 90 and score <= 100:
            topPerformers.append(float(score))
            pass
        pass
    for score in topPerformers:
        average += score
        pass
    average = Decimal(halfUpRound(average / float(len(topPerformers)))).quantize(Decimal("1.00"))
    print(average)
    
def halfUpRound(num):
    num_as_list = list(repr(num))
    last_digit = num_as_list[-1]
    if num_as_list[-2] == ".":
        # num is a float with only one digit after '.'
        digit_before = num_as_list[-3]
        db_pos = -3
        pass
    else:
        digit_before = num_as_list[-2]
        db_pos = -2
        pass
    new_num = ""
    #print(num)
    #print(last_digit)
    #print(digit_before)
    if int(last_digit) > int(digit_before):
        num_as_list.pop(-1)
        num_as_list.pop(db_pos)
        num_as_list.append(str(int(digit_before) + 1))
        pass
    else:
        num_as_list.pop(-1)
        pass
    if num_as_list[-1] == ".":
        num_as_list.pop(-1)
        pass
    new_num = ''.join(num_as_list)
    return float(new_num)

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = float(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
