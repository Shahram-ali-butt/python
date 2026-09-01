class Graph:
    def __init__(self):
        self.adjList = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def add_edge(self, src, des, directed = False):
        self.add_vertex(src)
        self.add_vertex(des)
        self.adjList[src].append(des)
        if not directed:
            self.adjList[des].append(src)

    def print(self):
        for vertex in self.adjList:
            print(vertex, '->', self.adjList[vertex])

'''
(1)--------(2)
 |          |
 |         (5)
 |          |
(3)--------(4)

No Zero-based indexing required 
'''

g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(4, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(3, 5)
g.print()

