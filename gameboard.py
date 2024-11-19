WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


class TicTacToe:

    def __init__(self):
        self.board = None

    def display_board(self, board):
        self.create_board(board)

    def create_board(self, board):
        for row in range(3):
            print(f'{board[row][0]}  | {board[row][1]}  | {board[row][2]}')
            if row < 2:
                print('_____________')

    def check_win_condition(self, board):
        flattened_board = [cell for row in board for cell in row]

        for win_cond in WINNING_COMBINATIONS:
            if flattened_board[win_cond[0]] == flattened_board[win_cond[1]] == flattened_board[win_cond[2]] != " ":
                self.display_board(board)
                # print('YOU WIN.')
                return True

    def is_draw(self, board):
        flattened_board = [cell for row in board for cell in row]

        if " " not in flattened_board:
            self.display_board(board)
            # print("It's a Draw.")
            return True
        return False
