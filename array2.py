import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print("Welcome to the 'Battleship' game!")

results = []

while True:
    name = input("What's your name, player? ")

    board = [['~' for _ in range(7)] for _ in range(7)]
    ship = [(1, 1), (1, 2), (1, 3)]
    shots = 0

    while True:
        clear_screen()

        print("   A B C D E F G")
        print("  ---------------")
        for row in range(7):
            print(f"{row + 1} | {' '.join(board[row])}")

        print(f"Shots: {shots}")

        shot = input("Enter coordinates for your shot (e.g., A1): ").strip().upper()

        if len(shot) != 2 or shot[0] not in 'ABCDEFG' or not shot[1].isdigit():
            print("Invalid format. Try again!")
            input("Press Enter to continue...")
            continue

        col = 'ABCDEFG'.index(shot[0])
        row = int(shot[1]) - 1

        if row < 0 or row > 6 or col < 0 or col > 6:
            print("Coordinates out of bounds. Try again!")
            input("Press Enter to continue...")
            continue

        if board[row][col] != '~':
            print("You already shot here. Try another cell!")
            input("Press Enter to continue...")
            continue

        shots += 1

        if (row, col) in ship:
            print("Hit!")
            board[row][col] = 'H'
            ship.remove((row, col))
            input("Press Enter to continue...")
        else:
            print("Miss!")
            board[row][col] = 'M'
            input("Press Enter to continue...")

        if len(ship) == 0:
            print(f"Congratulations, {name}! You sank the ship in {shots} shots!")

            results.append((name, shots))

            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nPlayer rankings:")
                rank = 1
                for player in results:
                    print(f"{rank}. {player[0]} - {player[1]} shots")
                    rank += 1
                print("Thanks for playing!")
                exit()

            board = [['~' for _ in range(7)] for _ in range(7)]
            ship = [(1, 1), (1, 2), (1, 3)]
            shots = 0
            continue


