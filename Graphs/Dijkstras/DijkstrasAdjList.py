from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
    # print("HII")
    visited = {initial: 0}
    path = {}
    removed_nodes = defaultdict(int)
    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        removed_nodes[min_node] = 1
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            if removed_nodes[edge] == 0:
                weight = current_weight + graph.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

    return visited


if __name__ == '__main__':
    graph = Graph()
    graph.add_node(2)
    graph.add_node(9)
    graph.add_node(5)
    graph.add_node(7)
    graph.add_node(1)
    graph.add_edge(2, 9, 2)
    graph.add_edge(2, 7, 3)
    graph.add_edge(7, 9, 7)
    graph.add_edge(9, 5, 1)
    graph.add_edge(7, 1, 3)
    graph.add_edge(9, 1, 7)
    graph.add_edge(5, 1, 3)
    visit = dijsktra(graph, 2)
    print(visit)
