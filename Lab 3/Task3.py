from collections import defaultdict, deque

def iddfs(graph, start, goal, max_depth):
    def dls(node, goal, depth):
        if depth == 0 and node == goal:
            return [node]
        if depth > 0:
            for neighbor in graph[node]:
                path = dls(neighbor, goal, depth - 1)
                if path:
                    return [node] + path
        return None

    for depth in range(max_depth + 1):
        result = dls(start, goal, depth)
        if result:
            return result
    return None

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    start_queue = deque([start])
    goal_queue = deque([goal])

    start_visited = {start: [start]}
    goal_visited = {goal: [goal]}

    while start_queue and goal_queue:
        if (path := search_layer(graph, start_queue, start_visited, goal_visited)):
            return path
        if (path := search_layer(graph, goal_queue, goal_visited, start_visited)):
            return path[::-1]
    return None

def search_layer(graph, queue, visited, other_visited):
    current = queue.popleft()
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited[neighbor] = visited[current] + [neighbor]
            queue.append(neighbor)
            if neighbor in other_visited:
                return visited[neighbor] + other_visited[neighbor][1:]
    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Test IDDFS
print("IDDFS Path:", iddfs(graph, 'A', 'E', 3))

# Test Bidirectional Search
bidirectional_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
print("Bidirectional Search Path:", bidirectional_search(bidirectional_graph, 'A', 'G'))
