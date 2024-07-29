### Course: Python Developer (Zero to Mastery)
### Section: Testing in Python
### script.py: module to be tested

### simple function to be tested
def simpleFunction(aNumber=int()) -> int:
    if type(aNumber) is not int: aNumber = int()
    return aNumber + 5
