class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        # Print the board in a user-friendly way
        for i in range(3):
            print('|'.join(self.board[i * 3:(i + 1) * 3]))
            if i < 2:
                print('-----')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        if all([spot == letter for spot in self.board[row_ind * 3:(row_ind + 1) * 3]]):
            return True
        # Check the column
        col_ind = square % 3
        if all([self.board[col_ind + i * 3] == letter for i in range(3)]):
            return True
        # Check diagonals
        if square % 2 == 0:  # only check diagonals if square is even (0, 2, 4, 6, 8)
            if all([self.board[i] == letter for i in [0, 4, 8]]):
                return True
            if all([self.board[i] == letter for i in [2, 4, 6]]):
                return True
        return False

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None


def minimax(board, depth, maximizing_player):
    # Check for terminal states (win/loss/draw)
    if board.current_winner == 'O':  # AI is O
        return 1
    elif board.current_winner == 'X':  # Human is X
        return -1
    elif len(board.available_moves()) == 0: 
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, depth + 1, False)
            board.board[move] = ' '  # Undo move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, depth + 1, True)
            board.board[move] = ' '  # Undo move
            min_eval = min(min_eval, eval)
        return min_eval


def best_move(board):
    best_score = float('-inf')
    move = None
    for possible_move in board.available_moves():
        board.make_move(possible_move, 'O') 
        score = minimax(board, 0, False)
        board.board[possible_move] = ' '
        
        if score > best_score:
            best_score = score
            move = possible_move
            
    return move


def play_game():
    game = TicTacToe()
    game.print_board()

    while True:
        # Human's turn (X)
        human_move = int(input("Enter your move (0-8): "))
        
        if not game.make_move(human_move, 'X'):
            print("Invalid move. Try again.")
            continue
        
        game.print_board()
        
        if game.current_winner:
            print("You win!")
            break
        
        if len(game.available_moves()) == 0:
            print("It's a draw!")
            break
        
        # AI's turn (O)
        ai_move = best_move(game)
        game.make_move(ai_move, 'O')
        
        game.print_board()
        
        if game.current_winner:
            print("AI wins!")
            break
        
        if len(game.available_moves()) == 0:
            print("It's a draw!")
            break


if __name__ == '__main__':
    play_game()