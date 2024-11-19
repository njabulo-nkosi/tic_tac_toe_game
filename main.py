from gameboard import TicTacToe
from player import Player

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
human_player = Player('Njabulo', 'X')
bot = Player('AI-Bot', 'O')
tic_tac_toe = TicTacToe()

board_display = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

tic_tac_toe.display_board(board_display)

while True:

    while True:
        try:
            player_choice = int(input('Please select a number from 0-8 to place your marker: '))
            if player_choice < 0 or player_choice > 8:
                print('Input must be between 0 and 8. Try again.')
                continue
        except ValueError:
            print('Invalid input. Please enter an number between 0-8.')
            continue

        if board[player_choice // 3][player_choice % 3] == " ":
            human_player.make_move(board, player_choice)
            break
        else:
            print('Position occupied. Please select another position.')

    if tic_tac_toe.check_win_condition(board):
        print(f'{human_player.name} Wins!')
        break

    if tic_tac_toe.is_draw(board):
        print("It's a Draw.")

    # Bot Turn
    bot.computer_player(board, None)
    if tic_tac_toe.check_win_condition(board):
        print(f'{bot.name} Wins!')
        break

    if tic_tac_toe.is_draw(board):
        print(f"It's a Draw.")
        break

    tic_tac_toe.display_board(board)
