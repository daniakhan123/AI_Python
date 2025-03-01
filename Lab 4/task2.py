import heapq
import random

def heuristic(node, goals):
    return min(abs(node[0] - g[0]) + abs(node[1] - g[1]) for g in goals)


def dynamic_astar(graph, start, goal):
    open_list = [(0, start, [start])]
    g_costs = {start: 0}

    while open_list:
        _, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return path
        
        for neighbor, cost in graph[current].items():
            new_cost = g_costs[current] + cost
            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                f_cost = new_cost + random.randint(1, 10)  # Simulate dynamic cost changes
                heapq.heappush(open_list, (f_cost, neighbor, path + [neighbor]))
    
    return None


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



# Run dynamic A* search
print("Optimal path with dynamic costs:", dynamic_astar(graph, 'A', 'F'))
