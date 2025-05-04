import random
import math

# Distance between two coordinates
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Total distance of a route
def total_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])

# Generate neighbors by swapping two locations
def generate_neighbors(route):
    neighbors = []
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]
            neighbors.append(new_route)
    return neighbors

# Hill Climbing algorithm
def hill_climb(locations, max_iterations=1000):
    current_route = locations[:]
    random.shuffle(current_route)
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_route)
        best_neighbor = min(neighbors, key=total_distance)
        best_distance = total_distance(best_neighbor)

        if best_distance < current_distance:
            current_route = best_neighbor
            current_distance = best_distance
        else:
            break  # No better neighbors → local optimum reached

    return current_route, current_distance
