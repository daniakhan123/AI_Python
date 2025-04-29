import sys
from collections import deque
import time
from ortools.sat.python import cp_model

class SudokuSolver:
    def __init__(self):
        self.solvers = {
            'AC3_Backtracking': self.solve_ac3,
            'OR_Tools': self.solve_or_tools,
            'Simple_Backtracking': self.solve_simple
        }
    
    def read_puzzles(self, filename):
        puzzles = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) == 81:
                    puzzle = []
                    for i in range(9):
                        row = []
                        for j in range(9):
                            char = line[i*9 + j]
                            row.append(0 if char == '.' else int(char))
                        puzzle.append(row)
                    puzzles.append((line, puzzle))
        return puzzles
    
    def format_solution(self, solution):
        return ''.join(str(solution[i][j]) for i in range(9) for j in range(9))
    
    # AC3 with Backtracking Implementation
    def solve_ac3(self, puzzle):
        class SudokuCSP:
            def __init__(self, puzzle):
                self.variables = [(i, j) for i in range(9) for j in range(9)]
                self.domains = {}
                self.constraints = []
                
                for i, j in self.variables:
                    value = puzzle[i][j]
                    if value != 0:
                        self.domains[(i, j)] = {value}
                    else:
                        self.domains[(i, j)] = set(range(1, 10))
                
                for i in range(9):
                    for j in range(9):
                        for k in range(9):
                            if k != j:
                                self.constraints.append(((i, j), (i, k)))
                        for k in range(9):
                            if k != i:
                                self.constraints.append(((i, j), (k, j)))
                        box_i, box_j = i // 3, j // 3
                        for x in range(box_i * 3, box_i * 3 + 3):
                            for y in range(box_j * 3, box_j * 3 + 3):
                                if x != i or y != j:
                                    self.constraints.append(((i, j), (x, y)))
            
            def is_consistent(self, X, x, Y, y):
                return x != y
            
            def revise(self, Xi, Xj):
                revised = False
                to_remove = set()
                for x in self.domains[Xi]:
                    has_support = False
                    for y in self.domains[Xj]:
                        if self.is_consistent(Xi, x, Xj, y):
                            has_support = True
                            break
                    if not has_support:
                        to_remove.add(x)
                        revised = True
                self.domains[Xi] -= to_remove
                return revised
            
            def ac3(self):
                queue = deque(self.constraints)
                while queue:
                    Xi, Xj = queue.popleft()
                    if self.revise(Xi, Xj):
                        if not self.domains[Xi]:
                            return False
                        for Xk in self.get_neighbors(Xi) - {Xj}:
                            queue.append((Xk, Xi))
                return True
            
            def get_neighbors(self, Xi):
                neighbors = set()
                for (X, Y) in self.constraints:
                    if X == Xi:
                        neighbors.add(Y)
                return neighbors
            
            def is_complete(self):
                for domain in self.domains.values():
                    if len(domain) != 1:
                        return False
                return True
            
            def is_assignment_consistent(self, var, value):
                i, j = var
                for y in range(9):
                    if y != j and (i, y) in self.domains and len(self.domains[(i, y)]) == 1 and value in self.domains[(i, y)]:
                        return False
                for x in range(9):
                    if x != i and (x, j) in self.domains and len(self.domains[(x, j)]) == 1 and value in self.domains[(x, j)]:
                        return False
                box_i, box_j = i // 3, j // 3
                for x in range(box_i * 3, box_i * 3 + 3):
                    for y in range(box_j * 3, box_j * 3 + 3):
                        if (x != i or y != j) and (x, y) in self.domains and len(self.domains[(x, y)]) == 1 and value in self.domains[(x, y)]:
                            return False
                return True
            
            def select_unassigned_variable(self):
                unassigned = [var for var in self.variables if len(self.domains[var]) > 1]
                return min(unassigned, key=lambda var: len(self.domains[var]))
            
            def order_domain_values(self, var):
                return sorted(self.domains[var])
            
            def backtracking_search(self):
                if self.ac3():
                    if self.is_complete():
                        return True
                    return self.backtrack()
                return False
            
            def backtrack(self):
                if self.is_complete():
                    return True
                var = self.select_unassigned_variable()
                for value in self.order_domain_values(var):
                    if self.is_assignment_consistent(var, value):
                        old_domain = self.domains[var]
                        self.domains[var] = {value}
                        if self.backtrack():
                            return True
                        self.domains[var] = old_domain
                return False
            
            def get_solution(self):
                solution = [[0]*9 for _ in range(9)]
                for i in range(9):
                    for j in range(9):
                        solution[i][j] = next(iter(self.domains[(i, j)]))
                return solution

        csp = SudokuCSP(puzzle)
        if csp.backtracking_search():
            return csp.get_solution()
        return None
    
    # OR-Tools Implementation
    def solve_or_tools(self, puzzle_str):
        model = cp_model.CpModel()
        grid = {}
        for i in range(9):
            for j in range(9):
                char = puzzle_str[i*9 + j]
                if char == '.':
                    grid[(i, j)] = model.NewIntVar(1, 9, f'cell_{i}_{j}')
                else:
                    grid[(i, j)] = model.NewIntVar(int(char), int(char), f'cell_{i}_{j}')
        
        for i in range(9):
            model.AddAllDifferent([grid[(i, j)] for j in range(9)])
        
        for j in range(9):
            model.AddAllDifferent([grid[(i, j)] for i in range(9)])
        
        for box_i in range(3):
            for box_j in range(3):
                model.AddAllDifferent([
                    grid[(i, j)]
                    for i in range(box_i * 3, box_i * 3 + 3)
                    for j in range(box_j * 3, box_j * 3 + 3)
                ])
        
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        
        if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            solution = [[0]*9 for _ in range(9)]
            for i in range(9):
                for j in range(9):
                    solution[i][j] = solver.Value(grid[(i, j)])
            return solution
        return None
    
    # Simple Backtracking Implementation
    def solve_simple(self, board):
        def is_valid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
            
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            start_row, start_col = row - row % 3, col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[i + start_row][j + start_col] == num:
                        return False
            return True
        
        def find_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        return (i, j)
            return None
        
        empty = find_empty(board)
        if not empty:
            return board
        
        row, col = empty
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve_simple(board):
                    return board
                board[row][col] = 0
        return None
    
    def compare_solvers(self, filename):
        puzzles = self.read_puzzles(filename)
        results = {name: {'time': 0, 'solved': 0} for name in self.solvers}
        
        for puzzle_str, puzzle in puzzles:
            for name, solver in self.solvers.items():
                start_time = time.time()
                if name == 'OR_Tools':
                    solution = solver(puzzle_str)
                else:
                    solution = solver([row.copy() for row in puzzle])
                elapsed = time.time() - start_time
                
                results[name]['time'] += elapsed
                if solution:
                    results[name]['solved'] += 1
        
        print("\nPerformance Comparison:")
        print("{:<20} {:<15} {:<15}".format('Solver', 'Total Time (s)', 'Puzzles Solved'))
        for name, data in results.items():
            print("{:<20} {:<15.4f} {:<15}".format(name, data['time'], data['solved']))
        
        fastest = min(results.items(), key=lambda x: x[1]['time'])
        print(f"\nFastest solver: {fastest[0]} ({fastest[1]['time']:.4f} seconds)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        sys.exit(1)
    
    solver = SudokuSolver()
    solver.compare_solvers(sys.argv[1])
