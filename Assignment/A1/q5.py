
import heapq

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu_Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu_Vilcea': 146, 'Pitesti': 138},
    'Rimnicu_Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu_Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

heuristics = { 
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100,
    'Rimnicu_Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80,
    'Vaslui': 199, 'Zerind': 374
}

# Breadth-First Search (BFS)
def bfs(start, goal):
    queue = [(start, [start])]
    visited = {start} 
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        for neighbor in romania_map[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Uniform Cost Search (UCS)
def ucs(start, goal):
    priority_queue = [(0, start, [start])]  
    visited = set()
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path, cost
        if node in visited:  
            continue
        visited.add(node)
        for neighbor, weight in romania_map[node].items():
            heapq.heappush(priority_queue, (cost + weight, neighbor, path + [neighbor]))
    return None

# Greedy Best First Search (GBFS)
def gbfs(start, goal):
    priority_queue = [(heuristics[start], start, [start])]
    visited = set()
    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        for neighbor in romania_map[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None

# Iterative Deepening Depth First Search (IDDFS)
def iddfs(start, goal, max_depth):
    def dls(node, goal, depth, path):
        if depth == 0 and node == goal:
            return path
        if depth > 0:
            for neighbor in romania_map[node]:
                result = dls(neighbor, goal, depth - 1, path + [neighbor])
                if result:
                    return result
        return None

    for depth in range(max_depth + 1):
        result = dls(start, goal, depth, [start])
        if result:
            return result
    return None


start_city = 'Arad'
goal_city = 'Bucharest'

print("BFS:", bfs(start_city, goal_city))
print("UCS:", ucs(start_city, goal_city))
print("GBFS:", gbfs(start_city, goal_city))
print("IDDFS:", iddfs(start_city, goal_city, 10))  
