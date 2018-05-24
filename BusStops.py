#!/bin/python3

import os
import sys

# Complete the minimumTimeToEnd function below.
def minimumTimeToEnd(x, w, v, q):
    # Take the descriptions of the people from standard input and print the answers to standard output
    bus_stops = x
    bus_time = w
    bus_speed = v
    num_people = q
    for i in range(num_people):
        # get person info
        person_info = list(input().split())
        person_pos = int(person_info[0])
        start_time = curr_time = int(person_info[1])
        #print("start: ", start_time, "current: ", curr_time)
        person_speed = int(person_info[2])
        # find dist to closest stop
        dist = 0
        closest_stop_dist = bus_stops[-1]
        closest_stop = bus_stops[-1]
        for stop in bus_stops:
            dist = abs(person_pos - stop)
            if dist < closest_stop_dist:
                closest_stop_dist = dist
                closest_stop = stop
        walk_time = closest_stop_dist / person_speed
        curr_time += walk_time # time after they walk
        #print("start: ", start_time, "current: ", curr_time)
        # add to time until bus comes
        wait_time = 0
        while curr_time % bus_time != 0:
            curr_time += 1 
            wait_time += 1
        dist_to_end = bus_stops[-1] - closest_stop
        ride_time = dist_to_end / bus_speed
        curr_time += ride_time
        total_time = curr_time - start_time
        #print("start: ", start_time, "current: ", curr_time)
        print("start_pos: {}, person_speed: {}, start_time: {}, closest_stop: {}, closest_stop_dist: {}, walk_time: {}, wait_time: {}, dist_to_end: {}, ride_time: {}".format(person_pos, person_speed, start_time, closest_stop, closest_stop_dist, walk_time, wait_time, dist_to_end, ride_time))
        print(total_time)
        
            

if __name__ == '__main__':
    n = int(input()) # number of stops
    x = list(map(int, input().rstrip().split())) # stop locations
    wv = input().split() 
    w = int(wv[0]) # time between buses
    v = int(wv[1]) # bus speed in meters per minute
    q = int(input()) # num of people
    minimumTimeToEnd(x, w, v, q)
