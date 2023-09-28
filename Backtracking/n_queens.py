"""
N Queens
There are n queens and a n*n chessboard. Place ALL the queens in such a way that no 2 queens ever a placed in each other's paths
This code gives all possible combinations
"""

# Function to check if two queens get in each others way
def isSafe(board, x, y):
    # return false if two queens share the same column
    for i in range(x):
        if board[i][y] == 1:
            return False
    # return false if two queens share the same `` diagonal
    (i, j) = (x, y)
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    # return false if two queens share the same `/` diagonal
    (i, j) = (x, y)
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True
 
 
def printSolution(board):
    for r in board:
        print(str(r))
    print()
 
 
def nQueen(board, n):
    # if all the queens are placed successfully, print the solution
    if n == len(board):
        printSolution(board)
        return
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(board)):
        # if no two queens threaten each other
        if isSafe(board, n, i):
            # place queen on the current square
            board[n][i] = 1
            # recur for the next row, the entire correct solution will come from here, other it will becktrack in the next line
            nQueen(board, n + 1)
            # backtrack and remove the queen from the current square
            board[n][i] = 0
 
 
if __name__ == '__main__':
    # size of the chessboard
    N = 8
    # the actual chessboard
    board = [[0 for x in range(N)] for y in range(N)]
    #starting the process of making all possible combinations of  n Queens on an n*n chessboard
    nQueen(board, 0)