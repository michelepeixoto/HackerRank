# Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

import re

print("Collatz Conjecture\n")
choice = "y"
while choice != "n":
    while True:
        num = input("Enter a number greater than one:\n")
        if re.match("^\d{1,10}$", num) and int(num)>1:
            n = int(num)
            break
        else:
            print("You must input a number greater than one.")
            continue
    steps = 0
    while n > 1:
        if n%2==0:
            n = n/2
            steps += 1
            pass
        else:
            n = n*3 + 1
            steps += 1
            pass
    print("\nIt took {} steps to reach 1 from {}.".format(steps, num))
    while True:
        choice = input("Try again? y/n\n")
        if choice == "n":
            quit()
            break
        elif choice == "y":
            break
        else:
            print("Invalid input.")
            continue

