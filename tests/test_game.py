import unittest
from unittest.mock import patch
import io
import sys
from src.game import play_game

class TestNumberGuessingGame(unittest.TestCase):

    @patch('src.game.random.randint')
    @patch('builtins.input')
    def test_correct_guess_on_first_try(self, mock_input, mock_randint):
        """Test if the game wins immediately when the first guess is correct."""
        # Force the secret number to be 50
        mock_randint.return_value = 50
        # Simulate the user entering '50'
        mock_input.return_value = "50"
        
        # Capture the printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        play_game()
        
        # Reset standard output
        sys.stdout = sys.__stdout__
        
        # Verify the success message is in the output
        self.assertIn("CONGRATULATIONS!", captured_output.getvalue())
        self.assertIn("in 1 attempts!", captured_output.getvalue())

    @patch('src.game.random.randint')
    @patch('builtins.input')
    def test_too_low_then_correct(self, mock_input, mock_randint):
        """Test handling of a 'Too low' guess followed by the correct guess."""
        mock_randint.return_value = 50
        # Simulate two consecutive inputs: first '30', then '50'
        mock_input.side_effect = ["30", "50"]
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        play_game()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn("Too low! Try again.", captured_output.getvalue())
        self.assertIn("in 2 attempts!", captured_output.getvalue())

    @patch('src.game.random.randint')
    @patch('builtins.input')
    def test_invalid_input_handling(self, mock_input, mock_randint):
        """Test if the game handles non-integer text inputs without crashing."""
        mock_randint.return_value = 50
        # Simulate invalid text 'abc', then the correct '50'
        mock_input.side_effect = ["abc", "50"]
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        play_game()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn("Invalid input! Please enter a valid whole number.", captured_output.getvalue())