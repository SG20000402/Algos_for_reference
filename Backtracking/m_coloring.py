"""
m coloring graph
Given a graph with vertices connected to each other. Connections are given.
Have to check if m colors can be applied in such a way that no 2 adjacent vertices are the same color.
"""

class Graph:

    #Function initializing the number of vertices and the connections of each vertex
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    #Checks if any adjacent vertex has the same color as that of selected vertex
    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    #thebacktracking function
    def graph_coloring_until(self, m, color, v):
        #Base case
        if v == self.V:
            return True
        
        #going through each color
        for c in range(1, m+1):
            if self.is_safe(v, color, c) == True:
                color[v] = c
                if self.graph_coloring_until(m, color, v+1) == True:
                    return True
                color[v] = 0


    def graph_coloring(self, m):
        color = [0]* self.V
        #starts the backtracking process
        if self.graph_coloring_until(m, color, 0) == 0:
            return False
        
        print('Solution exists and the following are the assigned colors: ')
        for i in color:
            print(i, end=" ")
        return True




if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 3
 
    # Function call
    g.graph_coloring(m)
 