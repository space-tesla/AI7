# Q.2 Write a Python program to solve 4 x 4 Queen problem.



def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_queens(board, col):
    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            if solve_queens(board, col + 1):
                return True

            board[row][col] = '.'

    return False

def solve_4_queens():
    board = [['.' for _ in range(4)] for _ in range(4)]

    if not solve_queens(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

solve_4_queens()


"""Output:
. Q . .
. . . Q
Q . . .
. . Q . """
