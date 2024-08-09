### Course: Zero to Mastery Academy | Python Developer
### Section: Testing in Python
### test_guessingGame.py: testing guessing_game.py module

### imports
import unittest
from guessing_game import verifyInteger

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

if __name__ == '__main__':
    unittest.main()
