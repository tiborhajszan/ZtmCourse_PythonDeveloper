### Course: Python Developer (Zero to Mastery)
### Section: Testing in Python
### test.py: testing script.py module

### imports
import unittest
import script

### unit test class
class ScriptTest(unittest.TestCase):

    ### test method: testing script > simple function
    def test_simpleFunction(self):
        test_param = 10
        test_result = script.simpleFunction(test_param)
        self.assertEqual(test_result, 10)

### running tests
unittest.main()
