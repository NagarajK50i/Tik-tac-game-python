    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def check_winner(board, player):
    # Check rows for win
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns for win
    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True

    # Check diagonals for win
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def make_move(board, player, row, col):
    if board[row][col] != '-':
        return False

    board[row][col] = player
    return True

def play_game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]

    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        valid_move = make_move(board, current_player, row, col)

        if not valid_move:
            print("Invalid move. Please try again.")
            continue

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            game_over = True

        current_player = 'O' if current_player == 'X' else 'X'

    if not game_over:
        display_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
