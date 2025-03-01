import heapq
import random

def heuristic(node, goals):
    return min(abs(node[0] - g[0]) + abs(node[1] - g[1]) for g in goals)

def best_first_search_with_goals(maze, start, goals):
    pq = [(heuristic(start, goals), start, [start])]
    visited = set()
    remaining_goals = set(goals)

    while pq and remaining_goals:
        _, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        
        if current in remaining_goals:
            remaining_goals.remove(current)
            if not remaining_goals:
                return path
        
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in maze and neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, remaining_goals), neighbor, path + [neighbor]))
    
    return None


# Example maze (grid with goals)
maze = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}
start = (0, 0)
goals = [(2, 1), (0, 2)]

# Example graph for A* with dynamic costs
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3, 'E': 2},
    'C': {'A': 2, 'F': 5},
    'D': {'B': 3},
    'E': {'B': 2, 'F': 1},
    'F': {'C': 5, 'E': 1}
}

# Run Best-First Search for multiple goals
print("Path covering all goals:", best_first_search_with_goals(maze, start, goals))

