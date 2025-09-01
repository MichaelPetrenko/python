import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Пример использования:
graph = {
'A': [('B', 2), ('C', 1)],
'B': [('C', 2), ('D', 1)],
'C': [('D', 4)],
'D': []
}
print(dijkstra(graph, 'A'))
# Вывод: {'A': 0, 'B': 2, 'C': 1, 'D': 3}