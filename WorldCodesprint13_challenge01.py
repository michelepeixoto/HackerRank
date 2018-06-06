#!/bin/python3

import os
import sys


class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def __str__(self):
        return self.name + " " + self.grade


class Group:
    
    def __init__(self):
        self.first_graders = 0
        self.second_graders = 0
        self.third_graders = 0
        self.students = []
        
    def __str__(self):
        s = ""
        for student in self.students:
            s += str(student) + "\n"
        return s
    
    def __len__(self):
        return len(self.students)
    
    def addStudents(self, *students):
        for student in students:
            if student.grade == "1":
                self.first_graders += 1
            elif student.grade == "2":
                self.second_graders += 1
            elif student.grade == "3":
                self.third_graders += 1
            self.students.append(student)
        
        
# Complete the membersInTheLargestGroups function below.
def membersInTheLargestGroups(n, m, a, b, f, s, t):
    # Print the names of the students in all largest groups or determine if there are no valid groups.
    total_students = n
    num_of_requests = m
    min_students = a
    max_students = b
    first_gr_max = f
    second_gr_max = s
    third_gr_max = t
    students = []
    # get all students
    for i in range(total_students):
        name, grade = input().split()
        student = Student(name, grade)
        #print(student)
        students.append(student)
    #print(students)
    groups = []
    total_groups = 0
    # process requests
    for i in range(num_of_requests):
        pair = input().split()
        for student in students:
            if student.name == pair[0]:
                student_one = student
            elif student.name == pair[1]:
                student_two = student
        pair = [student_one, student_two]
        #print(student_one, student_two)
        added_students = False
        student_one_group = None
        student_two_group = None
        # if there are no groups, add the pair to a new group
        if groups == []:
            newGroup = Group()
            newGroup.addStudents(student_one, student_two)
            groups.append(newGroup)
            #print("Added {} and {} to {}".format(student_one, student_two, groups.index(newGroup), newGroup))
        else:
            # see if students are in a group
            for group in groups:
                for student in group.students:
                    if student.name == student_one.name:
                        student_one_group = group
                        #print("student_one is in", group)
                    elif student.name == student_two.name:
                        student_two_group = group
                        #print("student_two is in", group)
            # if neither student is in a group
            if student_one_group == None and student_two_group == None:
                #print("Not in a group")
                # find a group that isn't at max capacity
                for group in groups:
                    if len(group) + 2 <= max_students:
                        group.addStudents(student_one, student_two)
                        #print("Added {} and {} to {}".format(student_one, student_two, group))
                        added_students = True
                # if all groups were at max capacity
                if added_students == False:
                    newGroup = Group()
                    newGroup.addStudents(student_one, student_two)
                    #print("Added {} and {} to {}".format(student_one, student_two, newGroup))
                    groups.append(newGroup)
            # if one student is in a group but the other student isn't
            elif student_one_group != None and student_two_group == None:
                # add student to group if it won't exceed capacity
                if len(student_one_group) + 1 <= max_students:
                    student_one_group.addStudents(student_two)
                    #print("Added {} and {} to {}".format(student_one, student_two, student_one_group))
            elif student_one_group == None and student_two_group != None:
                # add student to group if it won't exceed capacity
                if len(student_two_group) + 1 <= max_students:
                    student_two_group.addStudents(student_one)
                    #print("Added {} and {} to {}".format(student_one, student_two, student_two_group))
            # if both students are in different groups
            elif student_one_group != student_two_group:
                # combine groups if they will be under or at capacity
                if len(student_one_group) + len(student_two_group) <= max_students:
                    newGroup = Group()
                    newStudents = student_one_group.students + student_two_group.students
                    for student in newStudents:
                        newGroup.addStudents(student)
                        #print("Added {} to {}".format(student, newGroup))
                    groups.remove(student_one_group)
                    groups.remove(student_two_group)
                    groups.append(newGroup)
    # discard unsufficient groups
    for group in groups:
        if len(group) < min_students:
            #print("Discarding {} with {}".format(group, group.students))
            groups.remove(group)
    if groups == []:
        print("no groups")
    else:
        largest_group = 0
        for group in groups:
            #print(group)
            if len(group) > largest_group:
                largest_group = len(group)
        for group in groups:
            if len(group) == largest_group:
                for student in group.students:
                    print(student.name)
            
                
            
    
    

if __name__ == '__main__':
    nmabfst = input().split()

    n = int(nmabfst[0])

    m = int(nmabfst[1])

    a = int(nmabfst[2])

    b = int(nmabfst[3])

    f = int(nmabfst[4])

    s = int(nmabfst[5])

    t = int(nmabfst[6])

    membersInTheLargestGroups(n, m, a, b, f, s, t)
