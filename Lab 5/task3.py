import random
import math

# ---------- Utility Functions ----------
def distance(p1, p2):
    return math.dist(p1, p2)

def route_distance(route):
    return sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1)) + distance(route[-1], route[0])

def create_route(cities):
    route = cities[:]
    random.shuffle(route)
    return route

# ---------- Genetic Algorithm Components ----------
def initial_population(cities, size):
    return [create_route(cities) for _ in range(size)]

def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected.sort(key=route_distance)
    return selected[0]

def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end+1] = parent1[start:end+1]

    pointer = 0
    for city in parent2:
        if city not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = city
    return child

def mutate(route, mutation_rate=0.01):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

def next_generation(current_pop, elite_size=1, mutation_rate=0.01):
    new_pop = sorted(current_pop, key=route_distance)[:elite_size]  # Elitism
    while len(new_pop) < len(current_pop):
        parent1 = tournament_selection(current_pop)
        parent2 = tournament_selection(current_pop)
        child = ordered_crossover(parent1, parent2)
        mutate(child, mutation_rate)
        new_pop.append(child)
    return new_pop

# ---------- Main Genetic Algorithm ----------
def genetic_algorithm(cities, population_size=100, generations=500, mutation_rate=0.01):
    population = initial_population(cities, population_size)
    best_route = min(population, key=route_distance)
    
    for generation in range(generations):
        population = next_generation(population, elite_size=1, mutation_rate=mutation_rate)
        current_best = min(population, key=route_distance)
        if route_distance(current_best) < route_distance(best_route):
            best_route = current_best
        if generation % 50 == 0:
            print(f"Generation {generation}: Best Distance = {route_distance(best_route):.2f}")

    return best_route, route_distance(best_route)
