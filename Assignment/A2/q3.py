import time

def parse_grid(grid_string):
    """Convert grid string into a dictionary of {cell: digits}."""
    digits = '123456789'
    rows = 'ABCDEFGHI'
    cols = '123456789'
    squares = [r + c for r in rows for c in cols]
    
    values = {}
    for s, d in zip(squares, grid_string):
        if d == '0' or d == '.':
            values[s] = digits
        else:
            values[s] = d
    return values

def cross(A, B):
    return [a + b for a in A for b in B]

# Global variables for Sudoku
rows = 'ABCDEFGHI'
cols = '123456789'
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: set(sum(units[s], [])) - {s} for s in squares}

def is_solved(values):
    return all(len(values[s]) == 1 for s in squares)

def assign(values, s, d):
    """Eliminate all other values (except d) from values[s]."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2."""
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False  # Contradiction
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s2 for s2 in u if d in values[s2]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

def ac3(values):
    """AC-3 constraint propagation."""
    queue = [(s, p) for s in squares for p in peers[s]]
    while queue:
        (xi, xj) = queue.pop(0)
        if revise(values, xi, xj):
            if len(values[xi]) == 0:
                return False
            for xk in peers[xi] - {xj}:
                queue.append((xk, xi))
    return values

def revise(values, xi, xj):
    """Revise xi to remove inconsistent values."""
    revised = False
    for d in values[xi]:
        if len(values[xj]) == 1 and values[xj] == d:
            values[xi] = values[xi].replace(d, '')
            revised = True
    return revised

def select_unassigned_variable(values):
    """Choose the unassigned variable with the fewest possibilities."""
    unassigned = [s for s in squares if len(values[s]) > 1]
    return min(unassigned, key=lambda s: len(values[s]))

def backtrack(values):
    """Backtracking search."""
    if values is False:
        return False
    if is_solved(values):
        return values
    s = select_unassigned_variable(values)
    for d in values[s]:
        new_values = values.copy()
        if assign(new_values, s, d):
            attempt = backtrack(new_values)
            if attempt:
                return attempt
    return False

def solve(grid_string):
    """Solve a Sudoku puzzle."""
    values = parse_grid(grid_string)
    values = ac3(values)
    if values:
        values = backtrack(values)
    if values:
        result = ''.join(values[s] for s in squares)
        return result
    else:
        return None

def solve_file(filename):
    with open(filename, 'r') as file:
        puzzles = [line.strip() for line in file.readlines()]
    
    solutions = []
    start_time = time.time()
    for puzzle in puzzles:
        solution = solve(puzzle)
        solutions.append(solution)
    end_time = time.time()
    print(f"My CSP Solver Time: {end_time - start_time:.2f} seconds")
    
    return solutions

# Example
if __name__ == "__main__":
    solutions = solve_file("sudoku_input.txt")
    for sol in solutions:
        print(sol)
