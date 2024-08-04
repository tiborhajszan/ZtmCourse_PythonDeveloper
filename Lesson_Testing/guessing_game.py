### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### guessing_game.py: module to be tested

### imports
import random

### integer verification function
def verifyInteger(aInput=str()) -> bool:
    # asserting argument datatypes
    if type(aInput) is not str: aInput = str()
    # function main logic
    aInput = aInput.lstrip("-")
    if not aInput.isdecimal():
        print("Hey bozo, I expect an integer...")
        return False
    else: return True

### range verification function
def verifyRange(aNumber=int(), aStart=int(), aStop=int()) -> bool:
    # asserting argument datatypes
    if type(aNumber) is not int: aNumber = int()
    if type(aStart) is not int: aStart = int()
    if type(aStop) is not int: aStop = int()
    # function main logic
    if aNumber < aStart \
    or aStop < aNumber:
        print("Hey bozo, you are not figuring the range correctly...")
        return False
    else: return True

### guess evaluation function
def guessEval(aGuess=int(), aSecret=int()) -> bool:
    # asserting argument datatypes
    if type(aGuess) is not int: aGuess = int()
    if type(aSecret) is not int: aSecret = int()
    # function main logic
    if aGuess != aSecret:
        print("Wrong guess: Try again!")
        return False
    else:
        print("Guess what: You found me out!")
        return True

### game logic
if __name__ == "__main__":

    # obtaining range start
    while True:
        range_start = input("Guessing range start (must be an integer): ")
        if not verifyInteger(aInput=range_start): continue
        range_start = int(range_start)
        break

    # obtaining range stop
    while True:
        range_stop = input("Guessing range stop (must be an integer): ")
        if not verifyInteger(aInput=range_stop): continue
        range_stop = int(range_stop)
        if not verifyRange(aNumber=range_stop, aStart=range_start, aStop=range_stop): continue
        break

    # setting secret number
    secret_number = random.randint(range_start, range_stop)
    print(f"I thought of a number between {range_start} and {range_stop}. Can you find it out?")

    # guessing cycle
    while True:
        user_guess = input("Your guess (must be an integer): ")
        if not verifyInteger(aInput=user_guess): continue
        user_guess = int(user_guess)
        if not verifyRange(aNumber=user_guess, aStart=range_start, aStop=range_stop): continue
        if not guessEval(aGuess=user_guess, aSecret=secret_number): continue
        break
