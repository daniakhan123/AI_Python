import heapq

def greedy_bfs_delivery(graph, start, time_windows):
    visited = set()
    pq = [] 
    heapq.heappush(pq, (time_windows[start], start, [start], 0))  # (heuristic, node, path, time)
    
    best_path = []
    min_distance = float('inf')

    while pq:
        current_time, current, path, time = heapq.heappop(pq)
        
        if current in visited and len(path) != len(time_windows):
            continue
        visited.add(current)
        
        if len(path) == len(time_windows):
            if time < min_distance:
                best_path = path
                min_distance = time
            continue
        
        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                arrival_time = time + distance
                if arrival_time <= time_windows[neighbor]:
                    heapq.heappush(pq, (time_windows[neighbor], neighbor, path + [neighbor], arrival_time))

    return best_path, min_distance

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3, 'E': 2},
    'C': {'A': 2, 'F': 5},
    'D': {'B': 3},
    'E': {'B': 2, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

time_windows = {'A': 0, 'B': 5, 'C': 4, 'D': 8, 'E': 6, 'F': 10}

# Run Greedy Best-First Search
best_path, min_distance = greedy_bfs_delivery(graph, 'A', time_windows)
print("Optimized delivery path:", best_path)
print("Total travel distance:", min_distance)
