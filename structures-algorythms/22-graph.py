# Граф создается не с помощью списка - а с помощью словаря
# Ориентированный граф
class Graph:
    def __init__(self):
        self.graph = {}

    def add_graph(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

gr = Graph()
gr.add_graph("A", "B")
gr.add_graph("A", "C")
gr.add_graph("B", "C")
gr.print_graph()

# A -> ['B', 'C']
# B -> ['C']