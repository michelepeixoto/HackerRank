#!/bin/python3

import os
import sys

# takes in an array of 26 integers denoting the frequencies of the English letters and returns an integer denoting the maximum number of superior characters
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z

def maximumSuperiorCharacters(freq):
    word = []
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in range(len(freq)):
        for times in range(freq[char]):
            word.append(alphabet[char])
        #print("char pos: {}, char: {}, freq: {}".format(char, alphabet[char], freq[char]))
        pass
    word.append(word[1])
    word.pop(1)
    print(word)
    word_perm = []
    total_max = 0
    # eeilooos
    # eielooos
    while True:
        perm_max = 0
        for i in range(1, len(word)-1, 2):
            if alphabet.index(word[i+1]) > alphabet.index(word[i]):
                word.insert(i, word[i+1])
                word.pop(i+2)
                perm_max += 1
                if perm_max > total_max:
                    total_max = perm_max
                    pass
                print(word)
                pass
            pass
        if perm_max == 0:
            break
    return total_max    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        freq = list(map(int, input().rstrip().split()))

        result = maximumSuperiorCharacters(freq)

        fptr.write(str(result) + '\n')

    fptr.close()
