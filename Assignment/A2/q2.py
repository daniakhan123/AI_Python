import random

task_duration = [5, 8, 4, 7, 6, 3, 9]
facility_limits = [24, 30, 28]
operating_costs = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13],
]
penalty = 500

def createinitial(popsize):
    return [[random.randint(0,2) for _ in range(7)] for _ in range(popsize)]

def evaluate(solutions):
    costs = []
    for sol in solutions:
        total = 0
        usage = [0,0,0]
        for i,f in enumerate(sol):
            total += operating_costs[i][f] * task_duration[i]
            usage[f] += task_duration[i]
        for j in range(3):
            if usage[j] > facility_limits[j]:
                total += penalty
        costs.append(total)
    return costs

def selectparents(solutions, costs):
    ranked = sorted(zip(solutions, costs), key=lambda x: x[1])
    return [s for s,_ in ranked[:int(0.8*len(solutions))]]

def newgeneration(parents, popsize):
    children = []
    while len(children) < popsize:
        p1, p2 = random.sample(parents, 2)
        point = random.randint(1,6)
        child = p1[:point] + p2[point:]
        if random.random() < 0.2:
            child[random.randint(0,6)] = random.randint(0,2)
        children.append(child)
    return children[:popsize]

def optimize(popsize, gens):
    current = createinitial(popsize)
    bestsol = None
    bestcost = float('inf')
    for _ in range(gens):
        costs = evaluate(current)
        currentbest = min(costs)
        if currentbest < bestcost:
            bestcost = currentbest
            bestsol = current[costs.index(currentbest)]
        parents = selectparents(current, costs)
        current = newgeneration(parents, popsize)
    return bestsol, bestcost

bestsol, bestcost = optimize(6, 20)
print(bestsol, bestcost)

bestsol, bestcost = optimize(6, 30)
print(bestsol, bestcost)
