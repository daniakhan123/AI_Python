
import heapq

# DFS as Goal-Based Agent
def dfs_agent(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                stack.append((neighbor, path + [neighbor]))
    return None

# DLS as Goal-Based Agent
def dls_agent(graph, start, goal, depth_limit):
    def dls(node, path, depth):
        if node == goal:
            return path
        if depth == 0:
            return None
        for neighbor in graph.get(node, []):
            result = dls(neighbor, path + [neighbor], depth - 1)
            if result:
                return result
        return None
    
    return dls(start, [start], depth_limit)

# UCS as Utility-Based Agent
def ucs_agent(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, {}).items():
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

# Example graph (adjacency list with weights)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Run the agents
print("DFS Path:", dfs_agent(graph, 'A', 'F'))
print("DLS Path:", dls_agent(graph, 'A', 'F', 3))
print("UCS Path and Cost:", ucs_agent(graph, 'A', 'F'))
