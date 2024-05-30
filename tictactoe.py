import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def evaluate(board):
    for player in ['X', 'O']:
        if check_winner(board, player):
            return 1 if player == 'X' else -1

    return 0

def minimax(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, 'X'):
        return -1
    if check_winner(board, 'O'):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def ai_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, float('-inf'), float('inf'), False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    board[best_move[0]][best_move[1]] = 'O'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("~~~~~~~~~Tic-Tac-Toe!~~~~~~~~~~")
    print_board(board)

    while True:
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid option selected, Try again")
        print_board(board)

        if check_winner(board, 'X'):
            print("You win ... Somehow(Gotta check my code again)")
            break

        if is_board_full(board):
            print("Draw!")
            break

        print("AI is preparing a move")
        ai_move(board)
        print_board(board)

        if check_winner(board, 'O'):
            print("Defeat ... AI wins!.")
            break

        if is_board_full(board):
            print("Draw!")
            break

if __name__ == "__main__":
    play_game()
