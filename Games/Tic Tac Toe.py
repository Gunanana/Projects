import random

print("Tic-Tac-Toe:")
print("\nGAME RULES\n")
print("1. This is a 2 player game.")
print("2. Two signs represent each player. The general signs used in the game are X and O.")
print("3. There will be a board with 9 boxes.")
print("4. First, one user will place their sign in one of the available empty boxes.")
print("5. Next, the second user will place their sign in one of the available empty boxes.")
print("6. The goal of the players is to place their respective signs completely row-wise or column-wise, or diagonally.") 
print("7. Finally The game goes on until a player wins the game or it ended up in a draw by filling all boxes without a winning match.")
print("\nSYNTAX RULES\n")
print("1. Do not enter the coordinate of a box which is already filled, since the latest one will overwrite the previous one")
print("2. A space is a must between the row and column coordinate\n")
print("The Game begins. May the best player win!") 
class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self): 
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player}'s turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to mark spot: ").split()))
            print()

            # fixing the spot
            self.mark_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                print("Run it back?")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!\t")
                print("Up for a Rematch? Run the code.")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()