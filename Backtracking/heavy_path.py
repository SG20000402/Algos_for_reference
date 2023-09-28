"""
Heavy Path
Given a graph with vertices and paths connecting each other. The paths carry certain weights.
Check if there is any path in the system with total weight greater than the given target
"""

class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [[] for i in range(self.V)]

    def add_edge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def check_path(self, source, target):
        #Creating a path array and adding a source vertex
        path = [False]*self.V
        path[source] = 1
    
        return self.path_bkt(source, target, path)
    
    def path_bkt(self, source, target, path):
        #Base case
        if (target<=0):
            return True
        
        i = 0
        #Goes on for all the possible paths from source
        while i != len(self.graph[source]):

            #Recording the next vertex and weight
            v = self.graph[source][i][0]
            w = self.graph[source][i][1]
            i+=1
            
            #If vertex is already travelled, then ignore it and move on
            if(path[v] == True):
                continue

            #If weight of a path is greater than target, then we have found a path
            if (w>=target):
                return True
            #If not, we record that vertex as travelled and move on
            path[v] = True
            if (self.path_bkt(v, target-w, path)):
                return True
            
            path[v] = False

        return False


if __name__=="__main__":
    V = 9
    g = Graph(V)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    
    source = 0
    target = 62
    if g.check_path(source, target):
        print('Yes')
    else:
        print("No")

    target = 60
    if g.check_path(source, target):
        print("Yes")
    else:
        print("No")






