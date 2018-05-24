from random import randint

winningNum = randint(0, 1000000)
def guess(num):
    if num == winningNum:
        return "You win"
    elif num < winningNum:
        return "Too low"
    elif num > winningNum:
        return "Too high"

def play():
    maxNum = 1000000
    turns = 20
    myGuess = maxNum / 2
    minNum = 0
    while turns >= 0:
        answer = guess(myGuess)
        print("Guessed: {}\nAnswer: {}\nGuesses left: {}\n".format(myGuess, answer, turns))
        if answer == "Too low":
            minNum = myGuess
        elif answer == "Too high":
            maxNum = myGuess
        else:
            break
        myGuess = int(minNum + (maxNum - minNum) / 2)
        turns -= 1
    print("The correct number was",winningNum)
    
play()
