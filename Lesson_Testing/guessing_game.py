### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### guessing_game.py: module to be tested

### imports
import random

### integer verification function --------------------------------------------------------------------------------------
def verifyInteger(aInput=str()) -> bool:
    """
    Verifies if the provided input is a valid integer.

    Args:
        aInput (str): Input to verify. Defaults to an empty string if not provided or not string type.

    Returns:
        bool: True if the input is a valid integer, otherwise False.
    """

    ### asserting argument datatype
    if type(aInput) is not str: aInput = str()

    ### function main logic
    aInput = aInput.lstrip("-")
    if not aInput.isdecimal():
        print("The provided input is not an integer...")
        return False
    else:
        return True

### range verification function ----------------------------------------------------------------------------------------
def verifyRange(aInput=int(), aLow=int(), aHigh=int()) -> bool:
    """
    Verifies if the provided input is within a specified range.

    Args:
        aInput (int): Input to verify. Defaults to 0 if not provided or not integer type.
        aLow (int): Low boundary of the range. Defaults to 0 if not provided or not integer type.
        aHigh (int): High boundary of the range. Defaults to 0 if not provided or not integer type.

    Returns:
        bool: True if the input is within the range [aLow, aHigh], otherwise False.
    """

    ### asserting argument datatypes
    if type(aInput) is not int: aInput = int()
    if type(aLow) is not int: aLow = int()
    if type(aHigh) is not int: aHigh = int()

    ### function main logic
    if aInput < aLow or aHigh < aInput:
        print("The provided input is outside the expected range...")
        return False
    else:
        return True

### function obtaining guessing range low ------------------------------------------------------------------------------
def rangeLow() -> int:
    """
    Prompts the user to enter a valid integer for the guessing range low.
    Continues prompting until a valid integer is provided.

    Returns:
        rRange_low (int): valid integer provided by user as range low
    """

    ### function main logic
    while True:
        rRange_low = input("Guessing range low (must be an integer): ")
        if not verifyInteger(aInput=rRange_low): continue
        return int(rRange_low)

### function obtaining guessing range high -----------------------------------------------------------------------------
def rangeHigh(aLow=int()) -> int:
    """
    Prompts the user to enter a valid integer for the guessing range high.
    Ensures that the range high is larger than the range low.

    Args:
        aLow (int): lower bound of guessing range

    Returns:
        rRange_high (int): valid integer provided by user as range high
    """

    ### function main logic
    while True:
        rRange_high = input("Guessing range high (must be an integer): ")
        if not verifyInteger(aInput=rRange_high): continue
        rRange_high = int(rRange_high)
        if not verifyRange(aInput=rRange_high, aLow=aLow, aHigh=rRange_high): continue
        return rRange_high

### guess evaluation function ------------------------------------------------------------------------------------------
def guessEval(aGuess=int(), aSecret=int()) -> bool:
    """
    Evaluates whether a guess matches the secret number.

    Args:
        aGuess (int): guessed number, defaults to 0 if not provided or not integer type
        aSecret (int): secret number to be guessed, defaults to 0 if not provided or not integer type

    Returns:
        bool: True if guess matches secret number, otherwise False.
    """

    ### asserting argument datatypes
    if type(aGuess) is not int: aGuess = int()
    if type(aSecret) is not int: aSecret = int()

    ### function main logic
    if aGuess != aSecret: # wrong guess
        print("Wrong guess: Try again!")
        return False
    else: # correct guess
        print("Guess what: You found me out!")
        return True

### guessing cycle function --------------------------------------------------------------------------------------------
def guessingCycle(tLow=int(), tHigh=int(), tSecret=int()) -> None:
    """
    Executes a guessing cycle where the user is prompted to guess a secret number within a specified range.

    Args:
        tLow (int): low boundary of guessing range, defaults to 0 if not provided
        tHigh (int): high boundary of guessing range, defaults to 0 if not provided
        tSecret (int): secret number to be guessed, defaults to 0 if not provided

    Returns:
        None
    """

    ### guessing cycle
    while True:
        # prompting user for guess
        user_guess = input("Your guess (must be an integer): ")
        # guess is not integer > restart cycle
        if not verifyInteger(aInput=user_guess): continue
        # converting guess to integer
        user_guess = int(user_guess)
        # guess is outside range > restart cycle
        if not verifyRange(aInput=user_guess, aLow=tLow, aHigh=tHigh): continue
        # wrong guess > restart cycle
        if not guessEval(aGuess=user_guess, aSecret=tSecret): continue
        # correct guess > terminate cycle
        break

    ### returning
    return


########################################################################################################################


### game main logic
if __name__ == "__main__":
    range_low = rangeLow()
    range_high = rangeHigh(aLow=range_low)

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
