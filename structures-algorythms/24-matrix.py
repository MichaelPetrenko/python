class Graph:
    def __init__(self, graphs):
        self.V = graphs
        self.graph = [[0] * graphs for _ in range(graphs)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1

    def print_graph(self):
        for row in self.graph:
            print(row)

gm = Graph(4)
gm.add_edge(0, 1)
gm.add_edge(2, 0)
gm.add_edge(3, 1)
gm.add_edge(1, 0)
gm.print_graph()

# [0, 1, 0, 0]
# [1, 0, 0, 0]
# [1, 0, 0, 0]
# [0, 1, 0, 0]