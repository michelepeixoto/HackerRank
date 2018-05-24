# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 
# A player gets +1 point for each occurrence of the substring in the string.
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.

from collections import Counter


def minion_game(string):
    substrings_list = []
    substring = ""
    score = 0
    stuart = 0
    kevin = 0
    # generate all substrings:
    for x in range(len(string)+1):
        for y in range(x+1, len(string)+1):
            substring = string[x:y]
            #print(x, substring)
            substrings_list.append(substring)
            pass
        pass
    #print(substrings_list)
    substrings_dict = dict(Counter(substrings_list))
    #print(substrings_dict)
    # get scores:
    for item in substrings_dict:
        #print(item, substrings_dict[item])
        if is_vowel(item[0]):
            kevin += substrings_dict[item]
            pass
        else:
            stuart += substrings_dict[item]
            pass
        pass
    # print winner:
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
    pass


def is_vowel(letter):
    if letter in "AEIOU":
        #print(letter, "is a vowel")
        return True
    else:
        #print(letter, "is a consonant")
        return False
    pass
