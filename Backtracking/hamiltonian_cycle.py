"""
Hamiltonian Cycle
Graph matrix and vertices depicting the system which has been given. The matrix has 0s and 1s in which 1s show the 2 vertices are connected
and 0s show there's no connection between the vertices. Hamiltonian cycle is one in which ALL the vertices are traversed once and
we can end on the same vertex as which we started. 
Aim of this code is to make the possible Hamiltonian cycles. 
"""

class Hamiltonian:
    def __init__(self, start):
        #Start/end vertex
        self.start = start
        #List to store cycle path
        self.cycle = []
        #Checking if graph has cycle
        self.has_cycle = False
    
    def find_cycle(self):
        #Add starting vertex 
        self.cycle.append(self.start)
        #Starting the process of finding hamiltonian cycle
        self.solve(self.start)

    def solve(self, vertex):
        #Base condition: If end vertex is same as start vertex and all nodes have been visited
        if vertex == self.start and len(self.cycle) == N+1:
            self.has_cycle = True
            #Display the result
            self.display_cycle()
            #Will check for more cycles
            return

        #Iterating through neighbouring vertices
        for i in range(len(vertices)):
            if graph[vertex][i] == 1 and visited[i] == 0:
                nbr = i
                #Adds vertex to visited
                visited[nbr] = 1
                self.cycle.append(nbr)

                self.solve(nbr)

                visited[nbr] = 0
                self.cycle.pop()

    def display_cycle(self):
        names = []
        for v in self.cycle:
            names.append(vertices[v])
        print(names)





if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    graph = [[0, 1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 1, 0]]
    
    visited = [0 for _ in range(len(vertices))]

    N = 8

    hamiltonian = Hamiltonian(0)
    hamiltonian.find_cycle()

    if not hamiltonian.has_cycle:
        print("Hamiltonian does not exist")