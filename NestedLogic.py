# Your local library needs your help! Given the expected and actual return dates for a library book, create a 
# program that calculates the fine (if any). The fee structure is as follows:

# If the book is returned on or before the expected return date, no fine will be charged.
# If the book is returned after the expected return day but still within the same calendar month and year 
# as the expected return date, fine = 15 * number of days late.
# If the book is returned after the expected return month but still within the same calendar year as the 
# expected return date, fine = 500 * number of months late.
# If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000.


def calcFee(returned, due):
    # returned = due = {day: dd, month: mm, year: yyyy}
    fine = 0
    if returned['year'] < due['year']:
        fine = 0
    elif returned['year'] == due['year']:
        if returned['month'] < due['month']:
            fine = 0
        elif returned['month'] == due['month']:
            if returned['day'] <= due['day']:
                fine = 0
            else: 
                fine = 15 * (returned['day'] - due['day'])
        else:
            fine = 500 * (returned['month'] - due['month'])
    else:
        fine = 10000
    return fine



if __name__ == "__main__":
    returned, due = {}, {}
    r = [int(x) for x in input().split()]
    returned['day'] = r[0]
    returned['month'] = r[1]
    returned['year'] = r[2]
    d = [int(x) for x in input().split()]
    due['day'] = d[0]
    due['month'] = d[1]
    due['year'] = d[2]
    fine = calcFee(returned, due)
    print(fine)
            

# --------------------------------------- better way by @augustocmen ---------------------------------------
rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
# --------------------------------------- better way by @augustocmen ---------------------------------------