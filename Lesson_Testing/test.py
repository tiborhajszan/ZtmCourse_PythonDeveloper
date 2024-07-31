### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test.py: testing script.py module

### imports
import unittest
import script

### unit test class
class TestScript(unittest.TestCase):

    ### test method 1: testing script > simple function
    def test1_simpleFunction(self):
        test_result = script.simpleFunction()
        self.assertEqual(test_result, 5)
    
    ### test method 2: testing script > simple function
    def test2_simpleFunction(self):
        test_param = "pityu"
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 5)

    ### test method 3: testing script > simple function
    def test3_simpleFunction(self):
        test_param = 10
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 15)

### running tests
unittest.main()
