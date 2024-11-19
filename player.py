import random
from gameboard import WINNING_COMBINATIONS


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board, player_choice):
        if 0 <= player_choice <= 2:  # (player_choice >= 0 and player_choice <= 2)

            if board[0][player_choice] != " ":
                print('Current cell is occupied. Please choose a different position.')
                return
            board[0][player_choice] = self.symbol

        elif 3 <= player_choice <= 5:
            player_choice -= 3

            if board[1][player_choice] != " ":
                print('Current cell is occupied. Please choose a different position.')
                return
            board[1][player_choice] = self.symbol

        elif 6 <= player_choice <= 8:
            player_choice -= 6

            if board[2][player_choice] != " ":
                print('Current cell is occupied. Please choose a different position.')
                return
            board[2][player_choice] = self.symbol

    def computer_player(self, board, _):
        computer_choice = None
        flattened_board = [cell for row in board for cell in row]

        # check for move to win game
        for win_cond in WINNING_COMBINATIONS:
            if flattened_board[win_cond[0]] == flattened_board[win_cond[1]] == self.symbol and flattened_board[
                win_cond[2]] == " ":
                computer_choice = win_cond[2]
                break

        # check to block player win
        if computer_choice is None:
            for win_cond in WINNING_COMBINATIONS:
                if flattened_board[win_cond[0]] == flattened_board[win_cond[1]] != " " and flattened_board[
                    win_cond[2]] == " ":
                    computer_choice = win_cond[2]
                    break

        # else, select empty cell
        if computer_choice is None:
            available_moves = [index for index, value in enumerate(flattened_board) if value == " "]
            if available_moves:   # are there any move available
                computer_choice = random.choice(available_moves)
            else:
                return

        self.make_move(board, computer_choice)
