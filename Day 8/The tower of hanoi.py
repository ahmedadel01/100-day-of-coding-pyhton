"""The tower of hanoi."""

import copy
import sys

TOTAL_DISKS = 5 # more disks means a more difficult puzzle.

# Start with all disks on tower A:
SLOVED_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    """Runs a single game of the tower of hanoi."""
    print("""Move the tower of disks, one disk at a time, to another tower.
    Larger disks cannot rest on top of a smaller disk. """)

    """The towers dictionary has keys "A","B","C" and values 
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of 
    the list is the bottom of the tower. For a game with 5 disks,
    the list [5, 4, 3, 2, 1] represents a completed tower. The blank
    list [] represents a tower of no disks. The list [1, 3] has a 
    larger disk on top of a smaller disk and is an invalid
    configuration. The list [3, 1] is allowed since smaller disks
    can go on top of larger ones."""
    towers = {"A": copy.copy(SLOVED_TOWER), "B": [], "C": []}

    while True: # Run a single turn on each iteration of this loop.
        # display the towers and disks:
        displayTowers(towers)

        # Ask the user for a move :
        fromTower, toTower = getPlayerMove(towers)

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # check if the user has solved the puzzle:
        if SLOVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers) # Display the towers one last time.
            print("You have solved the puzzle! well done!")
            sys.exit()

def getPlayerMove(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True: # keep asking player until they enter a vaild move.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to moves a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Make sure the user entered valid tower letters:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter on of AB, AC, BA, BC, CA, or CB.")
            continue # Ask player again for their move.

        # Use mor descriptive variable names:
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # The "from" tower cannot ve an empty tower:
            print("You selected a tower with no disks.")
            continue # Ask player again for their move.
        elif len(towers[toTower]) == 0:
            # Any disk can be moved onto an empty "to" tower :
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue # Ask player again for their move.
        else:
            # This is avalid move, so return the selected towers:
            return fromTower, toTower

def displayTowers(towers):
    """Display the three towers with their disks."""

    # Display the three towers:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0) # Display the bare pole with no disk.
            else :
                displayDisk(tower[level]) # Display the disk.
        print()
    
    # Display the tower lables A, B and C :
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))

def displayDisk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        # Display the disk:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    main()
