### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test2.py: testing script.py module

### imports
import unittest
import script

### unit test class
class TestScript(unittest.TestCase):

    ### init method
    def setUp(self) -> None:
        print("\nTesting script.simpleFunction() Part2")
        return
    
    ### test 3
    def test3_simpleFunction(self) -> None:
        """Argument: str"""
        test_param = "pityu"
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, 5)
        return

    ### test 4
    def test4_simpleFunction(self) -> None:
        """Argument: int"""
        test_param = -10
        test_result = script.simpleFunction(aNumber=test_param)
        self.assertEqual(test_result, test_param+5)
    
    ### deinit method
    def tearDown(self) -> None:
        print("Test deinit")
        return

### running tests
if __name__ == "__main__":
    unittest.main()
