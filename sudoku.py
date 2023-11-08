def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True

    row, col = empty
    available_numbers = get_available_numbers(board, row, col)

    for num in available_numbers:
        board[row][col] = num
        print_board(board, row, col, "Trying")

        if solve_sudoku(board):
            return True

        board[row][col] = 0
        print_board(board, row, col, "Backtracking")

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def get_available_numbers(board, row, col):
    used_numbers = set(board[row]) | set(board[i][col] for i in range(9))
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    used_numbers |= set(board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))
    return [num for num in range(1, 10) if num not in used_numbers]

def print_board(board, row, col, message):
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    if message == "Trying":
        color = YELLOW
    elif message == "Solution":
        color = GREEN
    else:
        color = RED

    def print_separator():
        print("+-----+" + "-------+" + "-----+") 

    print(color + message + RESET)
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print_separator()
        if i == row:
            row_output = []
            for j in range(9):
                if j % 3 == 0 and j > 0:
                    row_output.append("|")
                if j == col:
                    row_output.append(f"{color}{board[i][j]}{RESET}" if board[i][j] != 0 else " ")
                else:
                    row_output.append(f"{board[i][j]}" if board[i][j] != 0 else " ")
            print(" ".join(row_output))
        else:
            row_output = []
            for j in range(9):
                if j % 3 == 0 and j > 0:
                    row_output.append("|")
                row_output.append(f"{board[i][j]}" if board[i][j] != 0 else " ")
            print(" ".join(row_output))
    print(RESET + "\n")


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print_board(puzzle, -1, -1, "Initial State")
if solve_sudoku(puzzle):
    print("Solved Sudoku:")
    print_board(puzzle, -1, -1, "Solution")
    input("Press Enter to exit...")
else:
    print("No solution exists.")
    input("Press Enter to exit...")
