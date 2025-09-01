import sys

def shortest_path(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        u = min((dist[v], v) for v in range(n) if not visited[v])[1]
        visited[u] = True

        for v in range(n):
            if graph[u][v] and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])
    return dist

# Пример использования:
graph = [
 [0, 2, 0, 1],
 [2, 0, 3, 2],
 [0, 3, 0, 4],
 [1, 2, 4, 0]
]
start = 0
print(shortest_path(graph, start)) # Вывод: [0, 2, 5, 1]