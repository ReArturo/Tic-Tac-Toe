import board_creation
import input_data

if __name__ == '__main__':
    new_board = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
    board_creation.display_board(new_board)
    input_data.player_input()
