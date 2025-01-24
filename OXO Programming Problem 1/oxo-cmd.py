"Note: This has been edited for Programming Problem 1"
import cmd
from oxo_logic import Game


class OxoCmd(cmd.Cmd):
    intro = "Welcome to Tic Tac Toe! Type 'help' or '?' to list commands.\n"
    prompt = "(oxo) "

    def __init__(self):
        super().__init__()
        self.game = Game()

    def do_new(self, arg):
        """Start a new game."""
        self.game.new_game()
        print("New game started!")
        print(self.game)

    def do_resume(self, arg):
        """Resume a saved game."""
        if self.game.restore_game():
            print("Game restored!")
        else:
            print("No saved game found. Starting a new game.")
        print(self.game)

    def do_save(self, arg):
        """Save the current game."""
        self.game.save_game()
        print("Game saved!")

    def default(self, line):
        """Handle unrecognized input as a move."""
        try:
            # Convert input to an integer and adjust for 0-based indexing
            cell = int(line) - 1
            if cell < 0 or cell >= 9:
                print("Invalid cell number. Please choose a number between 1 and 9.")
                return

            # User move
            result = self.game.make_move(cell)
            print(self.game)

            # Check game outcome after user move
            if result == "D":
                print("It's a draw!")
                self.game.new_game()
                print("New game started!")
                print(self.game)
                return
            elif result in ("X", "O"):
                print(f"The winner is: {result}!")
                self.game.new_game()
                print("New game started!")
                print(self.game)
                return

            # Computer move
            print("Computer's turn...")
            result = self.game.computer_move()
            print(self.game)

            # Check game outcome after computer move
            if result == "D":
                print("It's a draw!")
                self.game.new_game()
                print("New game started!")
                print(self.game)
            elif result in ("X", "O"):
                print(f"The winner is: {result}!")
                self.game.new_game()
                print("New game started!")
                print(self.game)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        except IndexError:
            print("Invalid move. Please choose a number between 1 and 9.")

    def do_quit(self, arg):
        """Quit the game."""
        print("Goodbye!")
        return True


def main():
    OxoCmd().cmdloop()


if __name__ == "__main__":
    main()
