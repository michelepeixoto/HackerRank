def cap(s):
    s_arr = []
    for word in s:
        s_arr.append(word)
    new_s = ""
    for i in range(len(s_arr)):
        if s_arr[i - 1] == " " or i == 0:
            new_s += s_arr[i].capitalize()
        else:
            new_s += s_arr[i]
    return new_s

if __name__ == "__main__":
    while True:
        s = input("What would you like to capitalize?\n")
        print(cap(s))
        choice = input("Quit? y/n\n")
        if choice == "y":
            break