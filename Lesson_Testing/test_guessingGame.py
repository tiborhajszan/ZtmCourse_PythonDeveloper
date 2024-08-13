### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test_guessingGame.py: testing guessing_game.py module

### imports
import unittest
from unittest import mock
from guessing_game import verifyInteger, verifyRange, rangeLow

### testing guessing_game.verifyInteger() ------------------------------------------------------------------------------
class TestVerifyInteger(unittest.TestCase):

    ### test the function with the default argument (empty string)
    def test_default_argument(self):
        self.assertFalse(verifyInteger())
    
    ### test when the input is not a string (defaults to empty string)
    def test_non_string_input(self):
        self.assertFalse(verifyInteger(789))
    
    ### test when the input is a string with only a negative sign (strips to empty string)
    def test_negative_sign_only(self):
        self.assertFalse(verifyInteger("-"))
    
    ### test when the input is an empty string (not decimal string)
    def test_empty_string(self):
        self.assertFalse(verifyInteger(""))
    
    ### test when the input is a string with spaces (not decimal string)
    def test_spaces_in_input(self):
        self.assertFalse(verifyInteger(" 123 "))
    
    ### test when the input contains non-numeric characters (not decimal string)
    def test_invalid_alphanumeric(self):
        self.assertFalse(verifyInteger("123abc"))
    
    ### test when the input is a floating-point number (not decimal string)
    def test_invalid_float(self):
        self.assertFalse(verifyInteger("123.45"))

    ### test when the input is a valid negative integer
    def test_valid_negative_integer(self):
        self.assertTrue(verifyInteger("-456"))
    
    ### test when the input is zero
    def test_valid_zero(self):
        self.assertTrue(verifyInteger("0"))

    ### test when the input is a valid positive integer
    def test_valid_positive_integer(self):
        self.assertTrue(verifyInteger("123"))

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

### testing guessing_game.rangeLow() -----------------------------------------------------------------------------------
class TestRangeLow(unittest.TestCase):

    ### test when a negative integer is provided as valid input
    @mock.patch('builtins.input', return_value='-15')
    def test_negative_integer_input(self, mock_input):
        self.assertEqual(rangeLow(), -15)
    
    ### test when zero is provided as valid input
    @mock.patch('builtins.input', return_value='0')
    def test_zero_input(self, mock_input):
        self.assertEqual(rangeLow(), 0)

    ### test when a positive integer is provided as valid input
    @mock.patch('builtins.input', return_value='5')
    def test_valid_input_first_attempt(self, mock_input):
        self.assertEqual(rangeLow(), 5)

    ### test when the first input is invalid and the second is valid
    @mock.patch('builtins.input', side_effect=['abc', '10'])
    def test_invalid_then_valid_input(self, mock_input):
        self.assertEqual(rangeLow(), 10)

    ### test when multiple invalid inputs are given before a valid one
    @mock.patch('builtins.input', side_effect=['abc', '', '7.5', '20'])
    def test_multiple_invalid_then_valid_input(self, mock_input):
        self.assertEqual(rangeLow(), 20)

### running the tests --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
