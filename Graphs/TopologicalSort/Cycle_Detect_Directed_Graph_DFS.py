from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.visited = [False] * V
        self.nodes = [False] * V

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def add_nodes(self, stack):
        for i in range(len(stack)):
            if stack[i]:
                self.nodes[i] = True

    def checkCycleInDirectedGraphUsingDFS(self, stack, v):
        self.visited[v] = True
        stack[v] = True
        for ele in self.graph[v]:
            if stack[ele]:
                self.add_nodes(stack)
                return
            elif not self.visited[ele]:
                self.checkCycleInDirectedGraphUsingDFS(stack, ele)
        stack[v] = False


if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    # g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    stack = [False] * 7
    if type(stack) == list:
        print('1')
    g.checkCycleInDirectedGraphUsingDFS(stack, 0)
    print(g.nodes)
