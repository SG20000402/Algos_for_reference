"""
Longest possible route with hurdles
Given a graph which contains obstacles, 
find the longest possible path from source to destination,
the user can only move up,down,left and right
and user cannot visit an already visited slot
"""

# Checking if the next cell to visit is valid, i.e, in the graph, and has not been traversed before
def isSafe(graph, visited, x, y):
    return 0 <= x < len(graph) and 0 <= y < len(graph[0]) and not (graph[x][y] == 0 or visited[x][y])
 
 
# Fbacktracking function
# max_dist —> keep track of the length of the longest path from source to destination
# dist —> length of the path from the source cell to the current cell (i, j)
def longest_path_bkt(graph, visited, source, dest, max_dist=0, dist=0):
    a, b = source
    # if the destination is not possible from the current cell
    if graph[a][b] == 0:
        return 0
 
    # if the destination is found, update `max_dist`
    if [a, b] == dest:
        return max(dist, max_dist)
 
    # set (i, j) cell as visited
    visited[a][b] = 1
 
    # go to the bottom cell
    if isSafe(graph, visited, a + 1, b):
        max_dist = longest_path_bkt(graph, visited, [a + 1, b], dest, max_dist, dist + 1)
 
    # go to the right cell
    if isSafe(graph, visited, a, b + 1):
        max_dist = longest_path_bkt(graph, visited, [a, b + 1], dest, max_dist, dist + 1)
 
    # go to the top cell
    if isSafe(graph, visited, a - 1, b):
        max_dist = longest_path_bkt(graph, visited, [a - 1, b], dest, max_dist, dist + 1)
 
    # go to the left cell
    if isSafe(graph, visited, a, b - 1):
        max_dist = longest_path_bkt(graph, visited, [a, b - 1], dest, max_dist, dist + 1)
 
    # backtrack: remove (i, j) from the visited matrix
    visited[a][b] = 0
 
    return max_dist
 
 
# Function to call the backtrackking function
def longest_path(graph, source, destination):
 
    # get source coordinates
    i, j = source
    
    # get destination coordinates
    x, y = destination

 
    # base case
    if not graph or len(graph) == 0 or graph[i][j] == 0 or graph[x][y] == 0:
        return 0
 
    # Creating a matrix to keep track of the visited cells
    visited = [[0 for x in range(len(graph[0]))] for y in range(len(graph))]

    return longest_path_bkt(graph, visited, source, destination)
 
 
if __name__ == '__main__':
 
    # input matrix
    graph = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
 
    source = [0, 0]
    destination = [5, 7]
 
    print("The maximum length path is", longest_path(graph, source, destination))
 
