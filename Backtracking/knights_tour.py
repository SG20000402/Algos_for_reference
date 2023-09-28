"""
Knight's tour
This algorithm is made to check the order in which a Knight will move on a chess board such that it covers all the squares.
"""


def isSafe(x,y,board):
  #checks whether the move is within the board or not.
  if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
    return True
  return False

def printSolution(board):
  for i in range(n):
        print(board[i]) 

def solveKT(board, pos_x, pos_y): 
  #refers to as solve Knight Tour. 
  #It provides a move to solveKTUil which says whether it’s true or false. 
  #Hence, it solves the problem by backtracking. 
  possible_moves = [[2,1], [1,2], [-1,2], [-2,1], [-2, -1], [-1, -2], [1, -2], [2,-1]]
  pos = 1
  if(not solveKTUtil(board, pos_x, pos_y, possible_moves, pos)): 
    print("Solution does not exist") 
  else: 
    printSolution(board) 


def solveKTUtil(board,curr_x,curr_y,moves,pos): 
  #function which receives a value from solveKT and check wethers it is valid or not.
  if(pos == n**2): 
    return True
  for i in range(8): 
    new_x = curr_x + moves[i][0] 
    new_y = curr_y + moves[i][1] 
    if(isSafe(new_x,new_y,board)): 
      board[new_x][new_y] = pos 
      if(solveKTUtil(board,new_x,new_y,moves,pos+1)): 
        return True
      board[new_x][new_y] = -1
  return False
    
if __name__ == "__main__":
    n=8
    board = [[-1 for i in range(n)]for i in range(n)] 
    board[0][7] = 0
    solveKT(board, 0, 7)
