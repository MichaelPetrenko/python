class WeightedGraph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u][v] = w
        self.graph[v][u] = w

    def print_graphs(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

gw = WeightedGraph()
gw.add_edge("A", "B", 1)
gw.add_edge("B", "C", 2)
gw.add_edge("C", "D", 0)
gw.add_edge("D", "E", 5)
gw.print_graphs()

# A -> {'B': 1}
# B -> {'A': 1, 'C': 2}
# C -> {'B': 2, 'D': 0}
# D -> {'C': 0, 'E': 5}
# E -> {'D': 5}