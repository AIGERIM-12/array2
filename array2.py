import os
import random
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to sea battle!")

grid = [['~' for _ in range(7)] for _ in range(7)]  
ships = []

ship_sizes = [3, 2, 2, 1, 1, 1, 1]

for size in ship_sizes:
    placed = False
    while not placed:
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        orientation = random.choice(["horizontal", "vertical"])
        
        if orientation == "horizontal" and col + size <= 7:
            if all(grid[row][col + i] == '~' for i in range(size)):
                ships.append([(row, col + i) for i in range(size)])
                placed = True
      
        elif orientation == "vertical" and row + size <= 7:
            if all(grid[row + i][col] == '~' for i in range(size)):
                ships.append([(row + i, col) for i in range(size)])
                placed = True
shots = 0
name = input("What's your name, player? ")
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
 
    print("   A B C D E F G")
    print("  ---------------")
    for row in range(7):
        print(f"{row + 1} | {' '.join(grid[row])}")
    
    print(f"Shots taken: {shots}")
    
    shot = input("Enter coordinates for your shot (e.g., A1): ").upper()

    if len(shot) != 2 or shot[0] not in 'ABCDEFG' or not shot[1].isdigit():
        print("Invalid input. Try again!")
        input("Press Enter to continue...")
        continue

    col = 'ABCDEFG'.index(shot[0])
    row = int(shot[1]) - 1

    
    if row < 0 or row > 6 or col < 0 or col > 6:
        print("Out of bounds. Try again!")
        input("Press Enter to continue...")
        continue

    if grid[row][col] != '~':
        print("You already shot here. Try another cell!")
        input("Press Enter to continue...")
        continue
    shots += 1
    hit = False
    for ship in ships:
        if (row, col) in ship:
            print("Hit!")
            grid[row][col] = 'H' 
            ship.remove((row, col))  
            hit = True
            break

    if not hit:
        print("Miss!")
        grid[row][col] = 'M'  

    input("Press Enter to continue...")

    
    if all(len(ship) == 0 for ship in ships):
        print(f"Congratulations, {name}! You sank all the ships in {shots} shots!")
        break

play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != 'yes':
    print("Thanks for playing!")



