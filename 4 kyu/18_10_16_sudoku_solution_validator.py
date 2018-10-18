# Write a function validSolution/ValidateSolution/valid_solution()
# that accepts a 2D array representing a Sudoku board, and returns
# true if it is a valid solution, or false otherwise. The cells of
# the sudoku board may also contain 0's, which will represent empty
# cells. Boards containing one or more zeroes are considered to be
# invalid solutions.
#
# The board is always 9 cells by 9 cells, and every cell only
# contains integers from 0 to 9.

from numpy import zeros, transpose
from itertools import product

def flip_row_cols(board):
    cols_board = zeros((9,9), dtype = int)
    for i in range(9):
        for j in range(9):
            cols_board[i][j] = board[j][i]
    return cols_board

def validSolution(board):

    nums = set(x for x in range(1,10))
    for row in board:
        if set(sorted(row)) != nums:
            return False

    flipped_board = flip_row_cols(board)
    for row in flipped_board:
        if set(sorted(row)) != nums:
            return False
    squares = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    cartesian_prod = product(squares, squares)
    for row, col in cartesian_prod:
        block = [board[r][c] for r, c in product(row, col)]
        if set(block) != nums:
            return False

    return True


def validSolution(board):
    nums = set(x for x in range(1,10))
    flipped_board = transpose(board)
    squares = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    cartesian_prod = product(squares, squares)

    for row in board:
        if set(sorted(row)) != nums:
            return False
    for row in flipped_board:
        if set(sorted(row)) != nums:
            return False
    for row, col in cartesian_prod:
        block = [board[r][c] for r, c in product(row, col)]
        if set(block) != nums:
            return False

    return True








print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 0, 3, 4, 9],
                     [1, 0, 0, 3, 4, 2, 5, 6, 0],
                     [8, 5, 9, 7, 6, 1, 0, 2, 0],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 0, 1, 5, 3, 7, 2, 1, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);

print(validSolution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [2, 3, 4, 5, 6, 7, 8, 9, 1],
                     [3, 4, 5, 6, 7, 8, 9, 1, 2],
                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                     [5, 6, 7, 8, 9, 1, 2, 3, 4],
                     [6, 7, 8, 9, 1, 2, 3, 4, 5],
                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                     [8, 9, 1, 2, 3, 4, 5, 6, 7],
                     [9, 1, 2, 3, 4, 5, 6, 7, 8]]), False)
