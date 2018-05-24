from random import randint

def makeArray():
    array = []
    for i in range(randint(0, 10)):
        array.append(randint(0,10))
    return array

def findClosestSum(array, x):
    smallestDiff = 20
    num1 = 0
    num2 = 0
    for num in array:
        for i in range(len(array) - 1):
            if i != array.index(num):
                sum = array[i] + num
                diff = abs(x - sum)
                if diff < smallestDiff:
                    smallestDiff = diff
                    num1 = array[i]
                    num2 = num
    print("Closest sum = {} + {}".format(num1, num2))

def main():
    array = makeArray()
    x = randint(0, 15)
    print(array)
    print("x =",x)
    findClosestSum(array, x)

main()
