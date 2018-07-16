# In the first line, print True if s has any alphanumeric characters. Otherwise, print False. 
# In the second line, print True if s has any alphabetical characters. Otherwise, print False. 
# In the third line, print True if s has any digits. Otherwise, print False. 
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False. 
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
def checkFor(s, case):
    p = False
    for char in s:
        if case == "isalnum":
            if char.isalnum():
                p = True
                break
        elif case == "isalpha":
            if char.isalpha():
                p = True
                break
        elif case == "isdigit":
            if char.isdigit():
                p = True
                break
        elif case == "islower":
            if char.islower():
                p = True
                break
        elif case == "isupper":
            if char.isupper():
                p = True
                break
    return p

if __name__ == '__main__':
    s = input()
    print(checkFor(s, "isalnum"))
    print(checkFor(s, "isalpha"))
    print(checkFor(s, "isdigit"))
    print(checkFor(s, "islower"))
    print(checkFor(s, "isupper"))