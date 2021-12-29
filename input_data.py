def player_input():
    """
    OUTPUT = player1, player2, marker
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Choose X or O: ').upper()
    if marker == 'X':
        print("player1 = X, Player2 = O")
        return 'X', 'O'

    else:
        print("player1 = O, Player2 = X")
        return 'O', 'X'
