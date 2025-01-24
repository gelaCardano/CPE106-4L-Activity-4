"Note: This has been edited for Programming Problem 1"
import random
import oxo_data


class Game:
    def __init__(self):
        """Initialize a new game with an empty board and set the first player as 'X'."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def new_game(self):
        """Start a new game by resetting the board."""
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def save_game(self):
        """Save the current game state to disk."""
        oxo_data.saveGame(self.board)

    def restore_game(self):
        """Restore a previously saved game state."""
        try:
            restored_board = oxo_data.restoreGame()
            if len(restored_board) == 9:
                self.board = restored_board
                return True
            else:
                self.new_game()
                return False
        except IOError:
            self.new_game()
            return False

    def make_move(self, cell):
        """
        Make a move for the current player.

        Args:
            cell (int): The cell index (0-8) where the move is made.

        Returns:
            str: 'X' or 'O' if the move resulted in a win, 'D' if the game is a draw, or an empty string if the game continues.
        """
        if self.board[cell] != " ":
            raise ValueError("Invalid cell")
        self.board[cell] = self.current_player

        if self.is_winning_move():
            return self.current_player
        elif self.is_draw():
            return "D"

        # Switch to the next player
        self.current_player = "O" if self.current_player == "X" else "X"
        return ""

    def computer_move(self):
        """Generate and make a move for the computer."""
        cell = self._generate_move()  # Get a random available cell
        if cell == -1:  # No available moves
            return "D"
        self.board[cell] = self.current_player  # Place 'O' on the board

        # Check for a win or draw after the move
        if self.is_winning_move():
            return self.current_player
        elif self.is_draw():
            return "D"

        # Switch back to the user's turn
        self.current_player = "X"
        return ""

    def _generate_move(self):
        """Generate a random move from the available cells."""
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def is_winning_move(self):
        """Check if the current move resulted in a win."""
        wins = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        )
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def is_draw(self):
        """Check if the game is a draw (no available cells)."""
        return all(cell != " " for cell in self.board)

    def __str__(self):
        """Return a string representation of the board."""
        return "\n".join([
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}",
            "-" * 9,
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}",
            "-" * 9,
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        ])
