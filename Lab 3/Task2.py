from itertools import permutations

def calculate_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # Return to starting city
    return distance

def tsp_bruteforce(graph):
    cities = list(graph.keys())
    min_distance = float('inf')
    best_path = []

    for perm in permutations(cities):
        current_distance = calculate_distance(perm, graph)
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = perm
    
    return best_path, min_distance

# Graph representing distances between cities
graph = {
    1: {2: 10, 3: 15, 4: 20},
    2: {1: 10, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 20, 2: 25, 3: 30}
}

best_path, min_distance = tsp_bruteforce(graph)
print("Shortest path:", best_path)
print("Minimum distance:", min_distance)
