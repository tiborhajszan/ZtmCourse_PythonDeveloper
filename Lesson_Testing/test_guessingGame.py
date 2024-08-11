### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test_guessingGame.py: testing guessing_game.py module

### imports
import unittest
from guessing_game import verifyInteger, verifyRange

### unittest class -----------------------------------------------------------------------------------------------------
class TestVerifyInteger(unittest.TestCase):
    """Tests guessing_game.verifyInteger function."""

    def test_valid_integer_positive(self):
        """Test with a valid positive integer as a string"""
        self.assertTrue(verifyInteger("123"))

    def test_valid_integer_negative(self):
        """Test with a valid negative integer as a string"""
        self.assertTrue(verifyInteger("-456"))

    def test_invalid_integer_with_letters(self):
        """Test with a string containing letters"""
        self.assertFalse(verifyInteger("12abc"))

    def test_invalid_integer_with_special_characters(self):
        """Test with a string containing special characters"""
        self.assertFalse(verifyInteger("!@#"))

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertFalse(verifyInteger(""))

    def test_non_string_input(self):
        """Test with a non-string input"""
        self.assertFalse(verifyInteger(123))

    def test_string_with_space(self):
        """Test with a string containing space"""
        self.assertFalse(verifyInteger("123 "))

### testing guessing_game.verifyRange() --------------------------------------------------------------------------------
class TestVerifyRange(unittest.TestCase):

    ### test the function with default arguments (all 0)
    def test_default_arguments(self):
        self.assertTrue(verifyRange()) # defaults to 0, so should return True

    ### test when the input is not an integer; it should default to 0
    def test_invalid_input_type(self):
        self.assertTrue(verifyRange("5", 0, 10)) # string input, defaults to 0
        self.assertTrue(verifyRange(15.5, 0, 10)) # float input, defaults to 0
        self.assertTrue(verifyRange([1, 2, 3], 0, 10)) # list input, defaults to 0
    
    ### test when the low boundary is not an integer; it should default to 0
    def test_invalid_low_type(self):
        self.assertTrue(verifyRange(5, "1", 10)) # string low boundary, defaults to 0
        self.assertTrue(verifyRange(5, 5.5, 10)) # float low boundary, defaults to 0
    
    ### test when the high boundary is not an integer; it should default to 0
    def test_invalid_high_type(self):
        self.assertFalse(verifyRange(5, 1, "10")) # string high boundary, defaults to 0
        self.assertFalse(verifyRange(5, 1, 10.5)) # float high boundary, defaults to 0
    
    ### test when all arguments are invalid types; they should all default to 0
    def test_invalid_all_arguments(self):
        self.assertTrue(verifyRange("input", "low", "high")) # all default to 0

    ### test when the input is below the specified range
    def test_below_range(self):
        self.assertFalse(verifyRange(0, 1, 10))
        self.assertFalse(verifyRange(-5, 1, 10))

    ### test when the input is within the specified range, including edge cases
    def test_within_range(self):
        self.assertTrue(verifyRange(5, 1, 10))
        self.assertTrue(verifyRange(1, 1, 10))
        self.assertTrue(verifyRange(10, 1, 10))

    ### test when the input is above the specified range
    def test_above_range(self):
        self.assertFalse(verifyRange(11, 1, 10))
        self.assertFalse(verifyRange(100, 1, 10))

### running the tests --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
