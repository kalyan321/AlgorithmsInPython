# Depth First Search

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.visited = [False] * vertices
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v):
        self.visited[v] = True
        for u in self.graph[v]:
            if not self.visited[u]:
                self.dfs(u)


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.dfs(0)

