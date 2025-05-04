import random

GRID_SIZE = 10

# Helper to convert grid coordinates like "B4" to (1,3)
def parse_coord(coord):
    row = ord(coord[0].upper()) - ord('A')
    col = int(coord[1:]) - 1
    return row, col

def print_grid(grid):
    print("  " + " ".join(str(i+1).rjust(2) for i in range(GRID_SIZE)))
    for r in range(GRID_SIZE):
        row_label = chr(ord('A') + r)
        print(row_label + " " + " ".join(grid[r][c] for c in range(GRID_SIZE)))

def place_ship(grid, ship_cells):
    for r, c in ship_cells:
        grid[r][c] = "S"

def is_hit(grid, r, c):
    return grid[r][c] == "S"

def mark_hit(grid, r, c):
    grid[r][c] = "X"

def mark_miss(grid, r, c):
    grid[r][c] = "O"

def all_ships_sunk(grid):
    return all(cell != "S" for row in grid for cell in row)

def get_adjacent_cells(r, c):
    return [(r+dr, c+dc) for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]
            if 0 <= r+dr < GRID_SIZE and 0 <= c+dc < GRID_SIZE]

# AI Strategy: randomly guesses, but if it hits, checks adjacent cells
class AIPlayer:
    def __init__(self):
        self.memory = []
        self.tried = set()

    def choose_move(self):
        if self.memory:
            for r, c in self.memory:
                for nr, nc in get_adjacent_cells(r, c):
                    if (nr, nc) not in self.tried:
                        self.tried.add((nr, nc))
                        return nr, nc
        # Random guess
        while True:
            r = random.randint(0, GRID_SIZE-1)
            c = random.randint(0, GRID_SIZE-1)
            if (r, c) not in self.tried:
                self.tried.add((r, c))
                return r, c

    def notify_result(self, r, c, result):
        if result == "Hit":
            self.memory.append((r, c))
        elif result == "Sunk":
            self.memory.clear()

# --- Game Setup ---

player_grid = [[" "]*GRID_SIZE for _ in range(GRID_SIZE)]
ai_grid = [[" "]*GRID_SIZE for _ in range(GRID_SIZE)]

# Example ships (length 3)
player_ships = [(3,4), (4,4), (5,4)]
ai_ships = [(1,1), (1,2), (1,3)]

place_ship(player_grid, player_ships)
place_ship(ai_grid, ai_ships)

ai = AIPlayer()

# --- Game Loop ---

while True:
    # Player turn
    print("\nYour Turn:")
    print_grid([[" " if cell == "S" else cell for cell in row] for row in ai_grid])
    move = input("Enter your attack (e.g., B4): ").strip().upper()
    if not move:
        continue
    r, c = parse_coord(move)
    if is_hit(ai_grid, r, c):
        mark_hit(ai_grid, r, c)
        print(f"Player attacks: {move} => Hit!")
        if all_ships_sunk(ai_grid):
            print("You sank all AI ships! You win!")
            break
    else:
        mark_miss(ai_grid, r, c)
        print(f"Player attacks: {move} => Miss.")

    # AI turn
    print("\nAI's Turn:")
    ar, ac = ai.choose_move()
    coord = f"{chr(ar+65)}{ac+1}"
    if is_hit(player_grid, ar, ac):
        mark_hit(player_grid, ar, ac)
        ai.notify_result(ar, ac, "Hit")
        print(f"AI attacks: {coord} => Hit!")
        if all_ships_sunk(player_grid):
            print("AI sank all your ships! You lose!")
            break
    else:
        mark_miss(player_grid, ar, ac)
        print(f"AI attacks: {coord} => Miss.")

