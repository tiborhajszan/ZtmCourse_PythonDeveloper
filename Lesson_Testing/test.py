### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test.py: testing script.py module

### imports
import unittest
import script

### unit test class
class TestScript(unittest.TestCase):

    ### test 1: testing script > simple function > no input
    def test1_simpleFunction(self):
        test_result = script.simpleFunction()
        self.assertEqual(test_result, 5)
    
    ### test 2: testing script > simple function > None input
    def test2_simpleFunction(self):
        test_param = None
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 5)
    
    ### test 3: testing script > simple function > string input
    def test3_simpleFunction(self):
        test_param = "pityu"
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 5)

    ### test 4: testing script > simple function > int input
    def test4_simpleFunction(self):
        test_param = -10
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, -5)

### running tests
if __name__ == "__main__":
    unittest.main()
