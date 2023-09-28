"""
Rat in a Maze
A rat is inside a maze, denoted by a square matrix, in which 0s denote dead ends and 1s denote a position which the rat can get to.
The rat can only move down, right, left and up 
Aim is to get to the  
"""

def is_valid(n, maze, x, y, result):    #This function checks if the given move is legal, ie, can the mouse move to it and if it's in the maze
    if x>=0 and y >= 0 and x < n and y < n and maze[x][y]==1 and result[x][y]==0:
        return True
    return False

def print_solution(board):
    for i in board:
        print(i)

def rat_running(n, maze, moves, pos_x, pos_y, res):
    #The backtracking function
    #First if statement is to set a full stop to the backtracking loop. 
    if pos_x==n-1 and pos_y==n-1:
        return True
    for i in moves:
    #Loops through all possible moves
    #Creates new position in each loop and checks if the new position is valid
        new_x = pos_x + i[0]
        new_y = pos_y + i[1]
        if is_valid(n, maze, new_x, new_y, res):
        #If new position is valid, the new position is added to the path and check possible paths from there
            res[new_x][new_y] = 1
            if rat_running(n, maze, moves, new_x, new_y, res):
            #If any path from there is valid, the resultant matrix is formed, and the backtracking process complete
            #If not, that path is closed off and we move to another path
                return True
            res[new_x][new_y] = 0
    return False
        
    
def rat_maze(n, maze):
    #Function which calls the backtracking function
    #First a resultant path matrix is created
    # Next the possible moves are made
    #Then the backtracking function is called which checks all possible paths
    # Once a successful path is formed, it is printed
    res = [[0 for i in range(4)] for i in range(4)]
    res[0][0] = 1
    moves = [[1,0], [0, 1], [-1, 0], [0, -1]]
    if rat_running(n, maze, moves, 0, 0, res):
        for i in res:
            print(i)




if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
              
    rat_maze(len(maze), maze)