# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def print_board(sudoku):
    """Print the board"""
    for row in range(9):
        print(sudoku[row][0:3], '|', sudoku[row][3:6], '|', sudoku[row][6:9])
        if row in (2, 5):
            print('-' * 33)


def update_board(sudoku):
    """Solve the board using recursion.  sudoku matrix is modified to contain the solution"""

    # Find first empty spot
    if (spot := find_empty(sudoku)) is None:
        return True  # No empty spots remaining.  Solved!!
    else:
        row, column = spot

    # Search for a number that fits in the empty spot
    for number in range(1, 10):
        if is_valid(sudoku, row, column, number):
            sudoku[row][column] = number
            if update_board(sudoku):  # Fill the next empty spot until no empty spots remain
                return True  # Puzzle solved

    # If we get here there were no valid numbers for this spot.  Set it back to empty
    sudoku[row][column] = 0

    # There are no solutions for the current board.  Undo the last spot and try again.
    return False


def is_valid(sudoku, row, column, number):
    """Return True if number can be placed in (row, column)"""

    # Look for matching number in the same row or column
    for i in range(9):
        if sudoku[i][column] == number or sudoku[row][i] == number:
            return False

    # Look for matching numbers in the same box
    row = row // 3 * 3
    column = column // 3 * 3
    for r in range(row, row + 3):
        for c in range(column, column + 3):
            if sudoku[r][c] == number:
                return False
    return True


def find_empty(sudoku):
    """Return row, column of first empty spot or None if no empty spots remain"""
    for row in range(9):
        try:
            # An empty spot contains 0
            return row, sudoku[row].index(0)
        except:
            pass
    return None


if __name__ == '__main__':
    sudoku = [
        [0, 0, 0, 3, 0, 0, 0, 7, 0],
        [7, 3, 4, 0, 8, 0, 1, 6, 2],
        [2, 0, 0, 0, 0, 0, 0, 3, 8],
        [5, 6, 8, 0, 0, 4, 0, 1, 0],
        [0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 7, 8, 0, 0, 2, 5, 4],
        [0, 7, 0, 0, 0, 2, 8, 9, 0],
        [0, 5, 1, 4, 0, 0, 7, 2, 6],
        [9, 0, 6, 0, 0, 0, 0, 4, 5]
    ]

    sudoku2 = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0,0 , 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7],
    ]
    print_board(sudoku)
    print("#" * 33)
    update_board(sudoku)
    print_board(sudoku)