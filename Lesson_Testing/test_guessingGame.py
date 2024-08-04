# Testing Guess Evaluation Function

# imports
import unittest
from To_Be_Sorted.GuessingGame import func_guessEval

# tester class
class EvalTest(unittest.TestCase):
    def test_none(self):
        test_result = func_guessEval("", 5)
        self.assertFalse(test_result)
    def test_intno(self):
        test_result = func_guessEval("0", 5)
        self.assertFalse(test_result)
    def test_intyes(self):
        test_result = func_guessEval("5", 5)
        self.assertTrue(test_result)
    def test_float(self):
        test_result = func_guessEval("5.14", 5)
        self.assertFalse(test_result)
    def test_str(self):
        test_result = func_guessEval("gibberish", 5)
        self.assertFalse(test_result)

# running tests
if __name__ == "__main__":
    unittest.main()
