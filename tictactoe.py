def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}, make your move (row and column: 0, 1, or 2):")

        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("Cell already taken, choose a different one.")
                continue
            board[row][col] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two numbers between 0 and 2.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Draw":
                print("The game is a draw!")
            else:
                print(f"Player {winner} wins!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
