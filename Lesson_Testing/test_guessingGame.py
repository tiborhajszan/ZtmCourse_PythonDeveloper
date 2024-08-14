### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test_guessingGame.py: testing guessing_game.py module

### imports
import unittest
from unittest import mock
from guessing_game import verifyInteger, verifyRange, rangeLow, rangeHigh

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

    ### test function with default arguments (all 0)
    def test_default_arguments(self):
        self.assertTrue(verifyRange())

    ### test noninteger input (defaults to 0)
    def test_invalid_input_type(self):
        self.assertTrue(verifyRange(aInput="5", aLow=0, aHigh=10))
        self.assertTrue(verifyRange(aInput=15.5, aLow=0, aHigh=10))
        self.assertTrue(verifyRange(aInput=[1, 2, 3], aLow=0, aHigh=10))
    
    ### test noninteger range low (defaults to 0)
    def test_invalid_low_type(self):
        self.assertTrue(verifyRange(aInput=5, aLow="1", aHigh=10))
        self.assertTrue(verifyRange(aInput=5, aLow=5.5, aHigh=10))
    
    ### test noninteger range high (defaults to 0)
    def test_invalid_high_type(self):
        self.assertFalse(verifyRange(aInput=5, aLow=1, aHigh="10"))
        self.assertFalse(verifyRange(aInput=5, aLow=1, aHigh=10.5))
    
    ### test noninteger all arguments (they default to 0)
    def test_invalid_all_arguments(self):
        self.assertTrue(verifyRange(aInput="input", aLow="low", aHigh="high"))

    ### test integer input below specified range
    def test_below_range(self):
        self.assertFalse(verifyRange(aInput=0, aLow=1, aHigh=10))
        self.assertFalse(verifyRange(aInput=-5, aLow=1, aHigh=10))

    ### test integer input within specified range
    def test_within_range(self):
        self.assertTrue(verifyRange(aInput=5, aLow=1, aHigh=10))
        self.assertTrue(verifyRange(aInput=1, aLow=1, aHigh=10))
        self.assertTrue(verifyRange(aInput=10, aLow=1, aHigh=10))

    ### test integer input above specified range
    def test_above_range(self):
        self.assertFalse(verifyRange(aInput=11, aLow=1, aHigh=10))
        self.assertFalse(verifyRange(aInput=100, aLow=1, aHigh=10))

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

### testing guessing_game.rangeHigh() ----------------------------------------------------------------------------------
class TestRangeHigh(unittest.TestCase):

    ### test function with default argument (0)
    @mock.patch('builtins.input', return_value='5')
    def test_default_low_argument(self, mock_input):
        self.assertEqual(rangeHigh(), 5)

    ### test noninteger first input (string) and valid second input
    @mock.patch('builtins.input', side_effect=['notanumber', '30'])
    def test_invalid_then_valid_input(self, mock_input):
        self.assertEqual(rangeHigh(aLow=20), 30)
    
    ### test multiple invalid inputs and valid last input
    @mock.patch('builtins.input', side_effect=['abc', '8', '25'])
    def test_multiple_invalid_then_valid_input(self, mock_input):
        self.assertEqual(rangeHigh(aLow=10), 25)
    
    ### test integer first input lower than range low and valid second input
    @mock.patch('builtins.input', side_effect=['5', '20'])
    def test_high_range_lower_than_low(self, mock_input):
        self.assertEqual(rangeHigh(aLow=10), 20)

    ### test integer input equal to range low
    @mock.patch('builtins.input', return_value='10')
    def test_high_range_equal_to_low(self, mock_input):
        self.assertEqual(rangeHigh(aLow=10), 10)

    ### test integer input greater than range low
    @mock.patch('builtins.input', return_value='15')
    def test_valid_high_range(self, mock_input):
        self.assertEqual(rangeHigh(aLow=10), 15)
    
    ### test negative integer input greater than range low
    @mock.patch('builtins.input', return_value='-5')
    def test_negative_high_range(self, mock_input):
        self.assertEqual(rangeHigh(aLow=-10), -5)

### running the tests --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
