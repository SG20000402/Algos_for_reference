"""
All possible paths between 2 vertices
Given a graph with multiple vertices and given paths connecting them, 
find the posssible paths between selected 2 vertices
"""
from collections import defaultdict

class Graph:
    #Initialize vertices and the graph containing all possible paths
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
   
    def print_paths_bkt(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        #If the 'source' and 'destination' are the same, the path is printed, otherwise, each vertex that is connected to the 'source' and not visited
        # is conidered as a new 'source' and the function is executed with the new source 
        if u==d:
            print(path)
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.print_paths_bkt(i, d, visited, path)
        path.pop()
        visited[u] = False

    #Function which calls the backtracking function
    def print_paths(self, source, destination):
        visited = [False]*(self.V)
        path = []
        self.print_paths_bkt(source, destination, visited, path)


if __name__=='__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(4, 2)
    graph.add_edge(4, 3)

    src = 0
    dest = 3
    print("All possible paths from %d to %d:" %(src, dest))
    graph.print_paths(src, dest)