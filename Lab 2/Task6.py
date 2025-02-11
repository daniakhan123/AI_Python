
import time

def display_grid(grid):
    """Displays the 3x3 grid with room statuses."""
    print("\nCurrent Environment:")
    for row in grid:
        print(" ".join(row))
    print("\n")

def firefighting_robot():
    # Initialize the 3x3 grid with room labels and fire status
    grid = [["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "j"]]
    
    fire_status = {
        'a': " ", 'b': " ", 'c': "🔥",
        'd': " ", 'e': "🔥", 'f': " ",
        'g': " ", 'h': " ", 'j': "🔥"
    }
    
    path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
    
    for room in path:
        print(f"Robot enters room '{room}'")
        
        if fire_status[room] == "🔥":
            print(f"Fire detected in room '{room}'! Extinguishing...")
            fire_status[room] = " "
            print(f"Fire in room '{room}' has been extinguished!")
        
        # Update and display the grid status
        updated_grid = [[fire_status[cell] for cell in row] for row in grid]
        display_grid(updated_grid)
        time.sleep(1)

    print("All rooms checked. No fires remaining!")

firefighting_robot()
