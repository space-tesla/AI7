# Q.2 Write a Python program to solve 4 x 4 Queen problem.


# Python program to solve the 4x4 Queen problem using backtracking

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to check if a queen can be placed at board[row][col]
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

# Function to solve the N-Queens problem using backtracking
def solve_queens(board, col):
    # If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing the queen in all rows one by one
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place queen on board[row][col]
            board[row][col] = 'Q'

            # Recur to place the rest of the queens
            if solve_queens(board, col + 1):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution, remove queen
            board[row][col] = '.'

    # If the queen cannot be placed in any row in this column, return false
    return False

# Function to initialize the board and solve the problem
def solve_4_queens():
    # Create a 4x4 chessboard initialized with '.'
    board = [['.' for _ in range(4)] for _ in range(4)]

    # Try to solve the 4-Queens problem
    if not solve_queens(board, 0):
        print("Solution does not exist")
        return False

    # If the solution is found, print the board
    print_board(board)
    return True

# Solve the 4x4 Queen problem
solve_4_queens()


Output:
. Q . .
. . . Q
Q . . .
. . Q .
