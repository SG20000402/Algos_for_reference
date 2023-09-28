"""
Sudoku solver
Given a sudoku puzzle, solve it using backtracking
"""

def print_sudoku(puzzle):
    for i in range(len(puzzle)):
        if (i%3 == 0 and i != 0):
            print('------------------------')
        for j in range(len(puzzle[0])):
            if (j%3==0 and j!=0):
                print("|", end=" ")
            print(puzzle[i][j], end=" ")
        print()

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i, j]

def is_valid(board, loc, val):
    #Checking row
    for i in range(len(board)):
        if board[loc[0]][i] == val and loc[1] != i:
            return False
    #Checking col
    for i in range(len(board)):
        if board[i][loc[1]] == val and loc[0] != i:
            return False
    #Checking box
    box_row = (loc[0]//3)*3
    box_col = (loc[1]//3)*3

    for i in range(box_row, box_col+3):
        for j in range(box_col, box_row+3):
            if board[i][j] == val and [i, j] != loc:
                return False
    return True



def solve(board):
    find = find_blank(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, [row, col], i):
            board[row][col] = i
            if solve(board):           
                return True
            board[row][col]=0
    return False




# puzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
#           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#           [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# puzzle = [[0, 0, 4, 3, 0, 0, 2, 0, 9], 
#           [0, 0, 5, 0, 0, 9, 0, 0, 1], 
#           [0, 7, 0, 0, 6, 0, 0, 4, 3], 
#           [0, 0, 6, 0, 0, 2, 0, 8, 7],
#           [1, 9, 0, 0, 0, 7, 4, 0, 0],
#           [0, 5, 0, 0, 8, 3, 0, 0, 0],
#           [6, 0, 0, 0, 0, 0, 1, 0, 5],
#           [0, 0, 3, 5, 0, 8, 6, 9, 0],
#           [0, 4, 2, 9, 1, 0, 3, 0, 0]]

# puzzle=[
#     [0, 8, 0, 5, 3, 0, 2, 7, 6],
#     [0, 5, 0, 6, 0, 0, 0, 0, 0], 
#     [6, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 6, 0, 5, 0, 0, 0, 0],
#     [0, 3, 2, 0, 0, 0, 7, 0, 1],
#     [7, 4, 5, 0, 0, 8, 6, 9, 3],
#     [0, 7, 0, 9, 6, 0, 5, 0, 0],
#     [4, 0, 0, 1, 8, 0, 0, 6, 7],
#     [5, 0, 0, 0, 0, 4, 8, 2, 9]
# ]

puzzle = [[7,8,0,4,0,0,1,2,0],
          [6,0,0,0,7,5,0,0,9],
          [0,0,0,6,0,1,0,7,8],
          [0,0,7,0,4,0,2,6,0],
          [0,0,1,0,5,0,9,3,0],
          [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2],
          [1,2,0,0,0,7,4,0,0],
          [0,4,9,2,0,6,0,0,7]]
solve(puzzle)
print_sudoku(puzzle)