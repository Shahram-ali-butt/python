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

    # Depth First Search
    def dfs(self, src):
        visited = [False]*self.size
        stack = [src]
        while(stack):
            v = stack.pop()
            if(visited[v] == False):
                print(v, end=" -> ")
                visited[v] = True
                
            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    stack.append(i)

    # Bre First Search
    def bfs(self, src):
        visited = [False]*self.size
        queue = [src]
        visited[src] = True
        while(queue):
            v = queue.pop(0)
            print(v, end=" -> ")
                
            for i in range(self.size):
                if(self.mat[v][i] == 1 and visited[i] == False):
                    queue.append(i)
                    visited[i] = True

'''
(0)----(2)----(3)----(5)
 |      |             |
(1)     ------(4)------
'''

g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.bfs(0)