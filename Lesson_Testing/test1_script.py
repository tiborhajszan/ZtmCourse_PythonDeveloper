### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test1_script.py: testing script.py module

### imports
import unittest
import script

### unit test class
class TestScript(unittest.TestCase):

    ### init method
    def setUp(self) -> None:
        print("\nTesting script.simpleFunction() Part1")
        return

    ### test 1
    def test1_simpleFunction(self) -> None:
        """Argument: no"""
        test_result = script.simpleFunction()
        self.assertEqual(test_result, 5)
        return
    
    ### test 2
    def test2_simpleFunction(self) -> None:
        """Argument: None"""
        test_param = None
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 5)
        return
    
    ### deinit method
    def tearDown(self) -> None:
        print("Test deinit")
        return

### running tests
if __name__ == "__main__":
    unittest.main()
