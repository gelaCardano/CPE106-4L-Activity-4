import unittest
import oxo_logic
import oxo_data
import os

class TestOxoLogic(unittest.TestCase):

    def setUp(self):
        """Set up a new game before each test."""
        self.game = oxo_logic.newGame()

    def tearDown(self):
        """Clean up saved game files after tests."""
        if os.path.exists("oxo_save.txt"):
            os.remove("oxo_save.txt")

    def test_new_game(self):
        """Test if a new game initializes with an empty board."""
        self.assertEqual(self.game, [" "] * 9)

    def test_user_move(self):
        """Test if a user move updates the board correctly."""
        oxo_logic.userMove(self.game, 0) 
        self.assertEqual(self.game[0], "X")

    def test_invalid_user_move(self):
        """Test if an invalid move raises a ValueError."""
        oxo_logic.userMove(self.game, 0)  
        with self.assertRaises(ValueError):
            oxo_logic.userMove(self.game, 0)  

    def test_computer_move(self):
        """Test if the computer move places an 'O' on the board."""
        result = oxo_logic.computerMove(self.game)
        self.assertIn("O", self.game) 
        self.assertIn(result, ["", "O", "D"]) 

    def test_is_winning_move(self):
        """Test if the game detects a winning move correctly."""
        self.game[0] = self.game[1] = self.game[2] = "X" 
        self.assertTrue(oxo_logic._isWinningMove(self.game))

    def test_is_not_winning_move(self):
        """Test if a non-winning board is detected correctly."""
        self.game[0] = "X"
        self.game[1] = "O"
        self.game[2] = "X"
        self.assertFalse(oxo_logic._isWinningMove(self.game))

    def test_draw(self):
        """Test if the game detects a draw correctly."""
        self.game = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        result = oxo_logic.computerMove(self.game)
        self.assertEqual(result, "D")  

    def test_restore_game(self):
        """Test if the game restores correctly from a save file."""
        self.game[0] = "X"
        oxo_logic.saveGame(self.game)
        restored_game = oxo_logic.restoreGame()
        self.assertEqual(restored_game, self.game)

if __name__ == "__main__":
    unittest.main()