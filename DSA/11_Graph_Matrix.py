class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for _ in range(vertex)]
        self.size = vertex

    def add_edge(self, src, des, weight: int = 1, directed: bool = False):
        if (0 <= src < self.size) and (0 <= des < self.size):
            self.mat[src][des] = weight
            if not directed:
                self.mat[des][src] = weight
        else:
            print("Error: Invalid Vertex")

    def print(self):
        for row in self.mat:
            print(' '.join(map(str, row)))

'''
(0)--------(1)
 |          |
 |         (4)
 |          |
(2)--------(3)

Zero-Based indexing required
'''

# # Undirected & Unweighted graph
# g = Graph(5)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 4)
# g.add_edge(2, 3)
# g.add_edge(3, 4)
# g.print()

# # Undirected & Weighted graph
# g = Graph(5)
# g.add_edge(0, 1, 3)
# g.add_edge(0, 2, 2)
# g.add_edge(1, 4, 1)
# g.add_edge(2, 3, 3)
# g.add_edge(3, 4, 1)
# g.print()

# # Directed & Unweighted graph
# g = Graph(5)
# g.add_edge(0, 1, 1, True)
# g.add_edge(0, 2, 1, True)
# g.add_edge(1, 4, 1, True)
# g.add_edge(2, 3, 1, True)
# g.add_edge(3, 4, 1, True)
# g.print()

# # Directed & Weighted graph
# g = Graph(5)
# g.add_edge(0, 1, 3, True)
# g.add_edge(0, 2, 2, True)
# g.add_edge(1, 4, 1, True)
# g.add_edge(2, 3, 3, True)
# g.add_edge(3, 4, 1, True)
# g.print()
