from pprint import pprint


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1,9):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][guess] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = "-1"
    return False

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == "-1":
                return r,c
    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)] 

    if guess in col_vals:
        return False

    row_starts = (row//3) *3
    col_starts = (col//3) *3

    for r in range(row_starts, row_starts+3):
        for c in range(col_starts, col_starts+3):
            if guess in puzzle[r][c]:
                return False
    return True


if __name__ == "__main__":
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(example_board))

    # pprint(example_board)