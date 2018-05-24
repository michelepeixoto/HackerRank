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
    average = twoDecRoundHalfUp(average / float(len(topPerformers)))
    print(average)
    
def twoDecRoundHalfUp(num):
    num_as_list = list(repr(num))
    round_pos = None
    # since num is float we will round after dot pos
    for i in range(len(num_as_list)):
        if num_as_list[i] == ".":
            round_pos = i
            pass
        pass
    # if float only goes up to one or two numbers after decimal, add zeroes
    if round_pos + 2 > len(num_as_list) - 1:
        num_as_list.append("0")
        pass 
    if round_pos + 3 > len(num_as_list) - 1:
        num_as_list.append("0")
        pass
    # if 3rd num after decimal is >= 5, round 2nd num up
    if int(num_as_list[round_pos + 3]) >= 5:
        # num is currently a str so we need to convert and revert
        num_as_list[round_pos + 2] = str(int(num_as_list[round_pos + 2]) + 1)
        pass
    # convert num list to a float with two decimals
    num_as_list = num_as_list[:round_pos + 3]
    #print(num_as_list)
    new_num = Decimal("".join(num_as_list))
    #print(type(new_num))
    return new_num

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = float(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
